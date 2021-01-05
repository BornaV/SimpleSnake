# Snake - DYOA at TU Graz WS 2020
# Name:       Borna Vincek
# Student ID: 11814996

import random

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
SNAKE = ["C3", "C2"]
ORIENTATION = 3

APPLE = "B1"
APPLE_LIVES = 10
APPLE_GOT_EATEN = False
LIVES = 3
SCORE = 0
BIGGER_SNAKE = False

ROW = []
COLUMN = []
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
userInputChar = ''
lastInput = ''
tempNextPosition = ""
validINPUT = False


def submit_score():
  NAME = input("Your name for the history:")
  temptxt = []
  temptxt.append("{0} - Score: {1} - Lives: {2} - Snake Length: {3}\n".format(NAME, SCORE, LIVES, len(SNAKE)))
  print("\n\nHistory:")
  file1 = open("history.txt","a")# makes sure that the history.txt exists
  file1.close()
  file1 = open("history.txt","r")
  for submissions in file1:
    temptxt.append(submissions)
    if len(temptxt) > 4:
      del temptxt[-1]
  file1.close()
  file1 = open("history.txt","w")
  for achievement in temptxt:
    print(achievement) 
    file1.write(achievement)
  file1.close()
  pass

def spawn_apple(state):
  global APPLE
  global APPLE_LIVES
  global APPLE_GOT_EATEN
  global BIGGER_SNAKE
  global LIVES
  temp = 0
  
  if state == 1:
    APPLE = generateApple()
    APPLE_LIVES = 10
    temp = 1
  if state == 2 and APPLE == SNAKE[-1]:
    BIGGER_SNAKE = True
    APPLE_GOT_EATEN = True
    APPLE = "00"
    temp = 1
  if APPLE_GOT_EATEN == True and state == 2:
    APPLE_GOT_EATEN = False
    APPLE = generateApple()
    APPLE_LIVES = 10
    temp = 1
  if APPLE_GOT_EATEN == False and state == 2 and APPLE_LIVES == 1:
    LIVES -= 1
    if LIVES == 0:
      submit_score()
      exit(0)
    APPLE = generateApple()
    APPLE_LIVES = 10
    temp = 1
  if temp == 0:
    APPLE_LIVES -= 1
  pass

def generateApple(): #generates the next temporary position of the apple
  cordinateEmpty = 1
  while cordinateEmpty != 0: 
    appleHeight = random.randint(0, BOARD_HEIGHT - 1)
    appleWidth = random.randint(0, BOARD_WIDTH - 1)
    cordinateEmpty = 0
    APPLEOld = APPLE
    for cordinate in SNAKE:
      if ALPHABET[appleHeight] == cordinate[0] and appleWidth == int(cordinate[1]):
        cordinateEmpty += 1
    if APPLEOld[0] == ALPHABET[appleHeight] and APPLEOld[1] == str(appleWidth):
      cordinateEmpty += 1 
  tempAPPLE = ALPHABET[appleHeight] + str(appleWidth)
  return tempAPPLE

def detect_collision():
  #test border width
  try:
    collisionTestCordinate = int(tempNextPosition[1])
  except ValueError:
    collisionTestCordinate = -1
  if collisionTestCordinate > BOARD_WIDTH -1 or collisionTestCordinate == -1 :
    return True
  #test border height
  collisionTestCordinate = tempNextPosition[0]
  letterInAlphabet = 0  
  while collisionTestCordinate != ALPHABET[letterInAlphabet]:
    letterInAlphabet += 1
  if letterInAlphabet > BOARD_HEIGHT - 1:
    return True
  #test itself
  iC = 0
  while iC < len(SNAKE) - 1:
    if SNAKE[iC] == tempNextPosition:
      return True
    iC += 1
  
  pass

def move_snake(userInputChar):
  global ORIENTATION
  global BIGGER_SNAKE
  if userInputChar == "w":
    ORIENTATION = 2
  if userInputChar == "s":
    ORIENTATION = 4
  if userInputChar == "a":
    ORIENTATION = 3
  if userInputChar == "d":
    ORIENTATION = 5
  SNAKE.append(getNextPos(userInputChar))
  if BIGGER_SNAKE == False:
    del SNAKE[0]
  BIGGER_SNAKE = False
  pass

def getNextPos(char): #get the next position of the snake
  global tempNextPosition
  tempNextPosLetter = SNAKE[-1]
  tempNextPosLetter = tempNextPosLetter[0]
  tempNextPosNumber = SNAKE[-1]
  tempNextPosNumber = tempNextPosNumber[1]
  tempNextPosNumber = int(tempNextPosNumber)
  letterInAlphabet = 0  
  while tempNextPosLetter != ALPHABET[letterInAlphabet]:
    letterInAlphabet += 1
  if char == "w":
    tempNextPosition = ALPHABET[letterInAlphabet - 1] + str(tempNextPosNumber)
  if char == "s":
    tempNextPosition = ALPHABET[letterInAlphabet + 1] + str(tempNextPosNumber)
  if char == "a":
    tempNextPosition = ALPHABET[letterInAlphabet] + str(tempNextPosNumber - 1)
  if char == "d":
    tempNextPosition = ALPHABET[letterInAlphabet] + str(tempNextPosNumber + 1)
  return tempNextPosition

def makeOrentation(ORIENTATION):#assign orientation to the correct symbol
  if ORIENTATION == 2:
    OrientationChar = '∧' 
  if ORIENTATION == 3:
    OrientationChar = '<'
  if ORIENTATION == 4:
    OrientationChar = 'v'
  if ORIENTATION == 5:
    OrientationChar = '>'
  return OrientationChar

def is_snake(row, column, part):
  if SNAKE[part] == '{0}{1}'.format(row,column):
    if len(SNAKE) - 1 == part:
      return ORIENTATION
    elif len(SNAKE) != part:
      return 1
    else:
      return 0

  pass

def is_apple(row, column):
  if APPLE == '{0}{1}'.format(row,column):
    return True
  else:
    return False
  pass

def print_game_board():
  if COLUMN == []:
   BDTL()
  print("Lives: {0} - Apple Lives: {1} - Score: {2}".format(LIVES, APPLE_LIVES, SCORE))
  print("----------------------------")
  for i in COLUMN :
    iC = ALPHABET[i]
    print("{0} |".format(ALPHABET[i]), end = '') 
    for j in ROW:
      iR = j
      iS = 0
      empty = True
      if empty == True:
        for k in SNAKE:
          k = k
          if is_snake(iC, iR, iS) == ORIENTATION and empty == True:
            print(' {0} '.format(makeOrentation(ORIENTATION)),  end = '')
            empty = False
          elif is_snake(iC, iR, iS) == 1 and empty == True:
            print(' + ',  end = '')
            empty = False
          iS += 1
      if is_apple(iC, iR) == True: #prints apple
          print(' O ',end = '')
          empty = False
      if empty == True:
        print('   ', end = '')
    print(" |")
  print("----------------------------")
  print("    ", end = '')
  for i in COLUMN :  
    print(" {0} ".format(COLUMN[i]), end = '')
  print()
  pass

def BDTL(): #board dimensions to list
  global COLUMN
  global ROW
  iC = 0
  iR = 0
  while BOARD_HEIGHT > len(COLUMN):
    COLUMN.append(iC)
    iC += 1
  while BOARD_WIDTH > len(ROW):
    ROW.append(iR)
    iR += 1
  pass

def DirToInput(): #on startup if unvalid input
  global ORIENTATION
  global lastInput
  if ORIENTATION == 2:
    lastInput = "w"
  if ORIENTATION == 4:
    lastInput = "s"
  if ORIENTATION == 3:
    lastInput = "a"
  if ORIENTATION == 5:
    lastInput = "d"

def userInput(userInputChar):
  global lastInput
  global validINPUT
  if userInputChar == "w":
    if ORIENTATION == 4:
      print("INVALID") #If you try to step backwards, print INVALID ||in the main function and print the previous screen again
      validINPUT = False
      return lastInput
    validINPUT = True
    lastInput = "w"
    return userInputChar

  elif userInputChar == "a":
    if ORIENTATION == 5:
      print("INVALID")
      validINPUT = False
      return lastInput
    validINPUT = True
    lastInput = "a"
    return userInputChar
    
  elif userInputChar == "s":
    if ORIENTATION == 2:
      print("INVALID")
      validINPUT = False
      return lastInput
    validINPUT = True
    lastInput = "s"
    return userInputChar
    
  elif userInputChar == "d":
    if ORIENTATION == 3:
      print("INVALID")
      validINPUT = False
      return lastInput
    validINPUT = True
    lastInput = "d"
    return userInputChar
  elif userInputChar == "":
    validINPUT = True
    return lastInput
  elif userInputChar == 'q':
    exit(0)
  else:
    validINPUT = True
    return lastInput
  
def main():
  global SCORE
  BDTL()
  DirToInput()
  #_6_spawn_apple(1)
  print_game_board()
  while 1 == 1:
    userInputChar = userInput(input("input [w a s d]:"))
    if validINPUT == True:
      move_snake(userInputChar)
      if detect_collision() == True:
        submit_score()
        exit(0)
      spawn_apple(2)

      SCORE += 1
    print_game_board()
  pass


if __name__ == '__main__':
  main()
