import pgzrun, random

WIDTH = 400
HEIGHT = 200

buttons = [Rect((55,160), (50, 30)), Rect((115,160), (50, 30)), Rect((175,160), (50, 30)), Rect((235,160), (50, 30)), Rect((295,160), (50, 30))]
buttonColours = [(254, 0, 0),(254, 150, 0),(250, 254, 0),(14, 169, 1),(0, 178, 255)]

buttonIndex = -1

code = [random.randint(0, 4), random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)]

print(code)

clickedButtons = []
guessNumber = 0
correctInPlace = 0
correctOutOfPlace = 0

RED = (200, 0, 0)
WHITE = (200, 200, 200)

win = 0

def drawDots(count, x, y, r, colour):
  for i in range(0, count):
    screen.draw.filled_circle((x, y + i * 10) , r, colour)
 
def draw():
  screen.draw.rect(Rect((5,5), (300, 105)), (255, 255, 255))
  screen.draw.rect(Rect((5,113), (300, 44)), (255, 255, 255))
  screen.draw.rect(Rect((345,5), (30, 105)), (255, 255, 255))
 
  for i in range(0, len(buttons)):
    screen.draw.filled_rect(buttons[i], buttonColours[i])
 
  for i in range(0, len(clickedButtons)):
    screen.draw.filled_rect(Rect((10 + guessNumber * 30, 10 + i * 25), (20, 20)), buttonColours[clickedButtons[i]])

  drawDots(correctInPlace, 14+(guessNumber-1) * 30, 120, 4, RED)
 
  drawDots(correctOutOfPlace, 28+(guessNumber-1) * 30, 120, 4, WHITE)

  if win == True:
    screen.draw.filled_rect(Rect((100, 40), (200, 100)), (0, 0, 0))
    screen.draw.text("You won!", (125, 80), color = "white", fontsize = 50)
   
    for i in range(0, len(code)):
        screen.draw.filled_rect(Rect((350, 10 + i * 25), (20, 20)), buttonColours[code[i]])
  else:
    if guessNumber >= 10:
      screen.draw.filled_rect(Rect((100, 40), (200, 100)), (0, 0, 0))
      screen.draw.text("You lost!", (125, 80), color = "white", fontsize = 50)
     
      for i in range(0, len(code)):
        screen.draw.filled_rect(Rect((350, 10 + i * 25), (20, 20)), buttonColours[code[i]])
   
def update(dt):
  global buttonIndex, clickedButtons, guessNumber, correctInPlace, correctOutOfPlace, win
  if len(clickedButtons) == 4:
    guessNumber += 1
    correctInPlace = 0
    correctOutOfPlace = 0
   
    c = code.copy()
    for i in range(0, len(clickedButtons)):
      if clickedButtons[i] == c[i]:
        correctInPlace += 1
        clickedButtons[i] = -1
        c[i] = -1
       
    for i in range(0, len(clickedButtons)):
      if clickedButtons[i] >= 0 and clickedButtons[i] in c:
        correctOutOfPlace += 1
        c[c.index(clickedButtons[i])] = -1
        clickedButtons[i] = -1
   
    clickedButtons = []
  elif buttonIndex >= 0:
    clickedButtons.append(buttonIndex)
    buttonIndex = -1

  if correctInPlace >= 4:
    win = True
  else:
    if guessNumber >= 10:
      win = False
   
def on_mouse_up(pos, button):
  global buttonIndex

  if guessNumber <= 9:
    for i in range(0, len(buttons)):
      if buttons[i].collidepoint(pos):
        buttonIndex = i

pgzrun.go()
