import pygame, sys
from pygame.locals import QUIT
from basicCalculator import *
from pygame import mixer
pygame.init()

woodTap = mixer.Sound("WoodTap.mp3")

#DEFINE GLOBAL VARIABLES
equationX = 355
equationY = 20
resultX = 355
resultY = 80
oprend1 = ""
oprend2 = ""
equationBuilder = ""
resultBuilder = ""
operator = ""
globalCurrentNumber = ""
#define constane varables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 360
HEIGHT = 480
#this states font for creating numbers and symbols to label buttons
font = pygame.font.SysFont('arial', 20)
print(pygame.font.get_fonts())
displayfont =  pygame.font.SysFont('freesansbold.ttf',size= 100)

font2 = pygame.font.SysFont('arial', 50)

#create ouput where anwser is shown.
OUTPUT_DISPLAY = pygame.Surface((360, 180))
OUTPUT_DISPLAY.fill(BLACK)

#BELOW are rects surfs for buttons and their colors
CLEAR_ALL_RECT = pygame.Rect((0, 180, 90, 72.4))
CLEAR_ALL_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
CLEAR_ALL_SURF.fill((90, 90, 90, 50))
clear_label = font.render("C", True, WHITE)

BACK_RECT = pygame.Rect(90, 180, 90, 72.4)
BACK_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
BACK_SURF.fill((90, 90, 90, 50))
back_label = font.render("DEL", True, WHITE)

DIVIDE_RECT = pygame.Rect(180, 180, 90, 72.4)
DIVIDE_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
DIVIDE_SURF.fill((90, 90, 90, 50))
divide_label = font.render("÷", True, WHITE)

MULTIPLY_RECT = pygame.Rect(270, 180, 90, 72.4)
MULTIPLY_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
MULTIPLY_SURF.fill((90, 90, 90, 50))
multiply_label = font.render("x", True, WHITE)

SEV_RECT = pygame.Rect(0, 252.4, 90, 72.4)
SEV_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
SEV_SURF.fill((128, 128, 128, 50))
sev_label = font.render("7", True, WHITE)

EIGH_RECT = pygame.Rect(90, 252.4, 90, 72.4)
EIGH_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
EIGH_SURF.fill((128, 128, 128, 50))
eight_label = font.render("8", True, WHITE)

NINE_RECT = pygame.Rect(180, 252.4, 90, 72.4)
NINE_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
NINE_SURF.fill((128, 128, 128, 50))
nine_label = font.render("9", True, WHITE)

MINUS_RECT = pygame.Rect(270, 252.4, 90, 72.4)
MINUS_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
MINUS_SURF.fill((90, 90, 90, 50))
minus_label = font.render("-", True, WHITE)

FOUR_RECT = pygame.Rect(0, 324.8, 90, 72.4)
FOUR_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
FOUR_SURF.fill((128, 128, 128, 50))
four_label = font.render("4", True, WHITE)

FIV_RECT = pygame.Rect(90, 324.8, 90, 72.4)
FIV_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
FIV_SURF.fill((128, 128, 128, 50))
fiv_label = font.render("5", True, WHITE)

SIX_RECT = pygame.Rect(180, 324.8, 90, 72.4)
SIX_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
SIX_SURF.fill((128, 128, 128, 50))
six_label = font.render("6", True, WHITE)

ADD_RECT = pygame.Rect(270, 324.8, 90, 72.4)
ADD_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
ADD_SURF.fill((90, 90, 90, 50))
add_label = font.render("+", True, WHITE)

ONE_RECT = pygame.Rect(0, 396.2, 90, 72.4)
ONE_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
ONE_SURF.fill((128, 128, 128, 50))
one_label = font.render("1", True, WHITE)

TWO_RECT = pygame.Rect(90, 396.2, 90, 72.4)
TWO_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
TWO_SURF.fill((128, 128, 128, 50))
two_label = font.render("2", True, WHITE)

THR_RECT = pygame.Rect(180, 396.2, 90, 72.4)
THR_SURF = pygame.Surface((90, 72.4), pygame.SRCALPHA)
THR_SURF.fill((128, 128, 128, 50))
thr_label = font.render("3", True, WHITE)

EQL_RECT = pygame.Rect(270, 396.2, 90, 145.8)
EQL_SURF = pygame.Surface((90, 145.8), pygame.SRCALPHA)
EQL_SURF.fill((255, 165, 0, 50))
eql_label = font.render("=", True, WHITE)

ZERO_RECT = pygame.Rect(0, 468.6, 180, 73.4)
ZERO_SURF = pygame.Surface((180, 73.4), pygame.SRCALPHA)
ZERO_SURF.fill((128, 128, 128, 50))
zero_label = font.render("0", True, WHITE)

DCML_RECT = pygame.Rect(180, 468.6, 90, 73.4)
DCML_SURF = pygame.Surface((90, 73.4), pygame.SRCALPHA)
DCML_SURF.fill((128, 128, 128, 50))
dcml_label = font.render(".", True, WHITE)

#button demensions: 90, 72.4
# set up for display
DISPLAYSURF = pygame.display.set_mode((360, 540))
DISPLAYSURF.fill(WHITE)

def show_buttonybois():
  DISPLAYSURF.blit(OUTPUT_DISPLAY, (0, 0))
  x_offset = 45 - (clear_label.get_width() / 2)
  y_offset = 36.2 - (clear_label.get_height() / 2)
  DISPLAYSURF.blit(  clear_label, (CLEAR_ALL_RECT.x + x_offset, CLEAR_ALL_RECT.y + y_offset))
  DISPLAYSURF.blit(CLEAR_ALL_SURF, (CLEAR_ALL_RECT.x, CLEAR_ALL_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), CLEAR_ALL_RECT, 1)

  x_offset = 45 - (back_label.get_width() / 2)
  y_offset = 36.2 - (back_label.get_height() / 2)
  DISPLAYSURF.blit(back_label, (BACK_RECT.x + x_offset, BACK_RECT.y + y_offset))
  DISPLAYSURF.blit(BACK_SURF, (BACK_RECT.x, BACK_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), BACK_RECT, 1)

  x_offset = 45 - (divide_label.get_width() / 2)
  y_offset = 36.2 - (divide_label.get_height() / 2)
  DISPLAYSURF.blit(divide_label, (DIVIDE_RECT.x + x_offset, DIVIDE_RECT.y + y_offset))
  DISPLAYSURF.blit(DIVIDE_SURF, (DIVIDE_RECT.x, BACK_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), DIVIDE_RECT, 1)

  x_offset = 45 - (multiply_label.get_width() / 2)
  y_offset = 36.2 - (multiply_label.get_height() / 2)
  DISPLAYSURF.blit(multiply_label, (MULTIPLY_RECT.x + x_offset, MULTIPLY_RECT.y + y_offset))
  DISPLAYSURF.blit(MULTIPLY_SURF, (MULTIPLY_RECT.x, MULTIPLY_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), MULTIPLY_RECT, 1)

  x_offset = 45 - (sev_label.get_width() / 2)
  y_offset = 36.2 - (sev_label.get_height() / 2)
  DISPLAYSURF.blit(sev_label, (SEV_RECT.x + x_offset, SEV_RECT.y + y_offset))
  DISPLAYSURF.blit(SEV_SURF, (SEV_RECT.x, SEV_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), SEV_RECT, 1)

  x_offset = 45 - (eight_label.get_width() / 2)
  y_offset = 36.2 - (eight_label.get_height() / 2)
  DISPLAYSURF.blit(eight_label, (EIGH_RECT.x + x_offset, EIGH_RECT.y + y_offset))
  DISPLAYSURF.blit(EIGH_SURF, (EIGH_RECT.x, EIGH_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), EIGH_RECT, 1)

  x_offset = 45 - (nine_label.get_width() / 2)
  y_offset = 36.2 - (nine_label.get_height() / 2)
  DISPLAYSURF.blit(nine_label, (NINE_RECT.x + x_offset, NINE_RECT.y + y_offset))
  DISPLAYSURF.blit(NINE_SURF, (NINE_RECT.x, NINE_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), NINE_RECT, 1)

  x_offset = 45 - (minus_label.get_width() / 2)
  y_offset = 36.2 - (minus_label.get_height() / 2)
  DISPLAYSURF.blit(minus_label, (MINUS_RECT.x + x_offset, MINUS_RECT.y + y_offset))
  DISPLAYSURF.blit(MINUS_SURF, (MINUS_RECT.x, MINUS_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), MINUS_RECT, 1)

  x_offset = 45 - (four_label.get_width() / 2)
  y_offset = 36.2 - (four_label.get_height() / 2)
  DISPLAYSURF.blit(four_label, (FOUR_RECT.x + x_offset, FOUR_RECT.y + y_offset))
  DISPLAYSURF.blit(FOUR_SURF, (FOUR_RECT.x, FOUR_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), FOUR_RECT, 1)

  x_offset = 45 - (fiv_label.get_width() / 2)
  y_offset = 36.2 - (fiv_label.get_height() / 2)
  DISPLAYSURF.blit(fiv_label, (FIV_RECT.x + x_offset, FIV_RECT.y + y_offset))
  DISPLAYSURF.blit(FIV_SURF, (FIV_RECT.x, FIV_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), FIV_RECT, 1)

  x_offset = 45 - (six_label.get_width() / 2)
  y_offset = 36.2 - (six_label.get_height() / 2)
  DISPLAYSURF.blit(six_label, (SIX_RECT.x + x_offset, SIX_RECT.y + y_offset))
  DISPLAYSURF.blit(SIX_SURF, (SIX_RECT.x, SIX_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), SIX_RECT, 1)

  x_offset = 45 - (add_label.get_width() / 2)
  y_offset = 36.2 - (add_label.get_height() / 2)
  DISPLAYSURF.blit(add_label, (ADD_RECT.x + x_offset, ADD_RECT.y + y_offset))
  DISPLAYSURF.blit(ADD_SURF, (ADD_RECT.x, ADD_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), ADD_RECT, 1)

  x_offset = 45 - (one_label.get_width() / 2)
  y_offset = 36.2 - (one_label.get_height() / 2)
  DISPLAYSURF.blit(one_label, (ONE_RECT.x + x_offset, ONE_RECT.y + y_offset))
  DISPLAYSURF.blit(ONE_SURF, (ONE_RECT.x, ONE_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), ONE_RECT, 1)

  x_offset = 45 - (two_label.get_width() / 2)
  y_offset = 36.2 - (two_label.get_height() / 2)
  DISPLAYSURF.blit(two_label, (TWO_RECT.x + x_offset, TWO_RECT.y + y_offset))
  DISPLAYSURF.blit(TWO_SURF, (TWO_RECT.x, TWO_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), TWO_RECT, 1)

  x_offset = 45 - (thr_label.get_width() / 2)
  y_offset = 36.2 - (thr_label.get_height() / 2)
  DISPLAYSURF.blit(thr_label, (THR_RECT.x + x_offset, THR_RECT.y + y_offset))
  DISPLAYSURF.blit(THR_SURF, (THR_RECT.x, THR_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), THR_RECT, 1)

  x_offset = 45 - (eql_label.get_width() / 2)
  y_offset = 72.4 - (eql_label.get_height() / 2)
  DISPLAYSURF.blit(eql_label, (EQL_RECT.x + x_offset, EQL_RECT.y + y_offset))
  DISPLAYSURF.blit(EQL_SURF, (EQL_RECT.x, EQL_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), EQL_RECT, 1)

  x_offset = 90 - (zero_label.get_width() / 2)
  y_offset = 36.2 - (zero_label.get_height() / 2)
  DISPLAYSURF.blit(zero_label, (ZERO_RECT.x + x_offset, ZERO_RECT.y + y_offset))
  DISPLAYSURF.blit(ZERO_SURF, (ZERO_RECT.x, ZERO_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), ZERO_RECT, 1)

  x_offset = 45 - (dcml_label.get_width() / 2)
  y_offset = 36.2 - (dcml_label.get_height() / 2)
  DISPLAYSURF.blit(dcml_label, (DCML_RECT.x + x_offset, DCML_RECT.y + y_offset))
  DISPLAYSURF.blit(DCML_SURF, (DCML_RECT.x, DCML_RECT.y))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 0), DCML_RECT, 1)


def update_elements():
  #digitDisplay = font2.render(equationBuilder+"02354557890", True, WHITE)
  digitDisplay = font2.render(equationBuilder, True, WHITE)
  x = digitDisplay.get_width()
  DISPLAYSURF.blit(digitDisplay,(equationX - x, equationY))
  #digitDisplay = font2.render(resultBuilder+"023545567890", True, WHITE)
  digitDisplay = font2.render(resultBuilder, True, WHITE)
  x = digitDisplay.get_width()
  DISPLAYSURF.blit(digitDisplay,(resultX - x, resultY))




#caption is set to Calculate stuff here.

def handle_buttonyboi_clicks():
  global equationX, equationY, equationBuilder, oprend1, oprend2, operator, resultBuilder, globalCurrentNumber
  if resultBuilder:
    resultBuilder = ""
  if ZERO_RECT.collidepoint(pygame.mouse.get_pos()):
    print("0 button clicked")
    woodTap.play()
    equationBuilder += "0"
    globalCurrentNumber += "0"

  if ONE_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("1 button clicked")
    woodTap.play()
    equationBuilder += "1"
    globalCurrentNumber += "1"
  
  if DCML_RECT.collidepoint(pygame.mouse.get_pos()):  
    print(". button clicked")
    woodTap.play()
    equationBuilder += "."
    globalCurrentNumber += "."

  if TWO_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("2 button clicked")
    woodTap.play()
    equationBuilder += "2"
    globalCurrentNumber += "2"
  
  if THR_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("3 button clicked")
    woodTap.play()
    equationBuilder += "3"
    globalCurrentNumber += "3"
  
  if FIV_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("5 button clicked")
    woodTap.play()
    equationBuilder += "5"
    globalCurrentNumber += "5"
  
  if EIGH_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("8 button clicked")
    woodTap.play()
    equationBuilder += "8"
    globalCurrentNumber += "8"
  
  if FOUR_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("4 button clicked")
    woodTap.play()
    equationBuilder += "4"
    globalCurrentNumber += "4"
  
  if SIX_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("6 button clicked")
    woodTap.play()
    equationBuilder += "6"
    globalCurrentNumber += "6"
  
  if NINE_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("9 button clicked")
    woodTap.play()
    equationBuilder += "9"
    globalCurrentNumber += "9"
  
  if SEV_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("7 button clicked")
    woodTap.play()
    equationBuilder += "7"
    globalCurrentNumber += "7"
  
  if CLEAR_ALL_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("CLEAR button clicked")
    woodTap.play()
    equationBuilder = ""
    
  if BACK_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("<- button clicked")
    woodTap.play()
    
  
  if DIVIDE_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("÷ button clicked")
    woodTap.play()
    equationBuilder += "÷"
    globalCurrentNumber += "÷"
  
  if MULTIPLY_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("X button clicked")
    woodTap.play()
    equationBuilder += "x"
    globalCurrentNumber += "x"
  
  if MINUS_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("- button clicked")
    woodTap.play()
    equationBuilder += "-"
    globalCurrentNumber += "-"
  
  if ADD_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("+ button clicked")
    woodTap.play()
    equationBuilder += "+"
    globalCurrentNumber += "+"
  
  if EQL_RECT.collidepoint(pygame.mouse.get_pos()):  
    print("= button clicked")

#display title
pygame.display.set_caption('Calculate Stuff Here')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
          handle_buttonyboi_clicks()
  
    show_buttonybois()
    update_elements()
    #print(displayfont.get_height())
    # temp = font2.render("=+-/8",True, (255, 255, 255))
  
    # DISPLAYSURF.blit(temp,(0, 0 ))
    pygame.display.update()
