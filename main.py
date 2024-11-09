import pygame
import random
import math
pygame.init()
happyburgur = pygame.image.load("happyburgur.png")
happyburgur = pygame.transform.scale(happyburgur, (60, 60))
burgurburger = pygame.image.load("burgerburgurburgor.png")
burgurburger = pygame.transform.scale(burgurburger, (60, 40))
scschroael = 0
movement = [0.0,0.0]
size = (600, 600)
left = pygame.K_LEFT
right = pygame.K_RIGHT
screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, (238,216,174), (0, 0, 600, 600))
gabooga = open("scscscscororrrieieee.txt", "r").read()
print("(" + gabooga + ")")
pygame.display.set_caption("hifdgfgdfufggh score: ") 
font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render('hgihigighduhguirdscoere:' + str(round(float(gabooga),0)), True, (252, 3, 232), (238,216,174))

class llllllllllllllleeeeeeeeeeeeeeevvvvvvvvvvvvvvvvvveeeeeeeeeeeeeeeelllllllllllllll():
  def __init__(self, numPatforms, minDist, maxDist):
    #print (numPatforms)
    self.numPatforms = numPatforms
    #print (self.numPatforms)
    self.minDist = minDist
    self.maxDist = maxDist
    self.gggggggggggggrrrrirnouoyernnnotyierrruubnoqd = []
    self.patforms = []
    self.generatedhorse = 0
    #generatedhorse = generatedlevell
    blastingexplodingpoofart = 0
    #this is the x variable for the great burgur bridge
    for mcchicen in range(15):
      gggggrriiouieiendddd = patform(blastingexplodingpoofart, 561)
      self.gggggggggggggrrrrirnouoyernnnotyierrruubnoqd.append(gggggrriiouieiendddd)
      self.patforms.append(gggggrriiouieiendddd)
      blastingexplodingpoofart += 50
    self.gjeoineoratie()
  def reetttpepprretteperrattaairreiitiieereaaertatet(self):
    #repeat
    for ffffvvvvfvfffifififfiivvivivivvvveieeieieaiaie in range (5):
      #five
      platform = patform(random.randint(50, 550), random.randint(self.generatedhorse - 170, self.generatedhorse))
      self.patforms.append(platform)
  def gjeoineoratie(self):
    ccoounieait = 0
    while not self.numPatforms == ccoounieait:
      if ccoounieait < 5:
        ppaatteeeieieieffrroororommmwheeewhwhewhewheyyyyy = random.randint(0, 170)
      elif ccoounieait < 10:
        ppaatteeeieieieffrroororommmwheeewhwhewhewheyyyyy = random.randint(170, 340)
      elif ccoounieait < 15:
        ppaatteeeieieieffrroororommmwheeewhwhewhewheyyyyy = random.randint(340, 510)
      else:
        ppaatteeeieieieffrroororommmwheeewhwhewhewheyyyyy = random.randint(-170, 0) 

      platform = patform(random.randint(50, 550), ppaatteeeieieieffrroororommmwheeewhwhewhewheyyyyy)
      # 1/250,000 chance for 2 platform to spawn in the same exact location if you only see 14 platform you are very lucky you have wise burgur luck
      # 2 breads is a mcbread 6 1/2 breads is a mcloaf
      self.patforms.append(platform)         
      ccoounieait += 1
      #make a random platform - c
      #add platform to array - c
      #increase count - c

  def mccow(self, pllaier):
    if -pllaier.hhiieeeiiieeostttcscohohrrroe - 170 < self.generatedhorse:
      self.generatedhorse -= 170
      self.reetttpepprretteperrattaairreiitiieereaaertatet()
  def updateScreen(self, pllaier):
    #if player.y + scroll > 300 update scroll
    global scschroael
    if pllaier.y + scschroael < 300:
      scschroael = 300 - pllaier.y
  def update(self, pllaier):
    #print("TBD")
    self.mccow(pllaier)
    for patform in self.patforms:
      patform.eeeeeeoldmacdonaldhadaetjhrhvuegthoivisjfrhuefhugieieio()
    self.updateScreen(pllaier)
    
class patform (pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.length = 60
    self.width = 40
    self.rect = burgurburger.get_rect(center = pygame.Vector2(x, y))
  def move(self):
    print("chonky cow")
  def eeeeeeoldmacdonaldhadaetjhrhvuegthoivisjfrhuefhugieieio(self):
    screen.blit(burgurburger, (self.x - self.width/2, self.y - self.length/2 + scschroael) )
  def update(self):
    print("TBD")
    
class foodses():
  def __init__(self, name, foodz, width, height):
    self.name = name
    self.foodz = foodz
    self.gravity = .03
    self.x = 300
    self.y = 500
    self.width = width
    self.height = height
    self.dx = 0
    self.dy = 0
    self.hhiieeeiiieeostttcscohohrrroe = 0
  def hhiieeeiiieeostttcscohohrrroee(self):
    if 510 - self.y > self.hhiieeeiiieeostttcscohohrrroe:
      self.hhiieeeiiieeostttcscohohrrroe = 510 - self.y
  def printInfo(self):
    print("Name of restarunt:", self.name)
    print("Type of foodz sold:", self.foodz)
  def jump(self, patforms):
    booooooeeiliieann = False
    for pat in patforms:
      if self.tuotschieing(pat):
        booooooeeiliieann = True
        ppppaaaaatttttfffrooemmm = pat
    if booooooeeiliieann == True:
      self.dy += -4
  def move(self):
    K = pygame.key.get_pressed()
    if K[left]:
      self.dx = -2
    elif K[right]:
      self.dx = 2
    else:
      self.dx = 0
  
  def kccohllideaie_mcchicenx(self, patform):
    return  (self.x - (self.width/2.0) < patform.x+(patform.width/2.0)) and (self.x + (self.width/2.0) > patform.x - (patform.width/2.0))
  def kccohllideaie_mcchiceny(self, patform):
    nneeiscxxt_why = self.dy + self.y + self.height/2 + self.gravity
    return nneeiscxxt_why >= patform.rect.top and patform.rect.top >= self.y + self.height/2
  def tuotschieing(self, patform):
      return self.kccohllideaie_mcchiceny(patform) and self.kccohllideaie_mcchicenx(patform)
  def updateFood(self, patforms):
    #print ("yes")
    self.move()
    self.x += self.dx
    if self.x - (self.width/2) > 600:
      self.x -= 600 + self.width;
    if self.x + (self.width/2) < 0:
      self.x += 600 + self.width;
    booooooeeiliieann = False
    for pat in patforms:
      if self.tuotschieing(pat):
        booooooeeiliieann = True
        ppppaaaaatttttfffrooemmm = pat
    if booooooeeiliieann is False:
      self.dy += self.gravity
      self.y += self.dy
      #print ("tagcalefa")
    else:
      self.y = ppppaaaaatttttfffrooemmm.rect.top - self.height/2
      self.dy = 0
      #print ("patform: " + str(ppppaaaaatttttfffrooemmm.rect.top))
    
  def update(self, patforms):
    self.updateFood(patforms)
    self.hhiieeeiiieeostttcscohohrrroee()
    #print(str(self.dx) + ", " + str(self.dy) + "\n" + str(self.x) + ", " + str(self.y))
    #print("high score: " + str(round(self.hhiieeeiiieeostttcscohohrrroe)))
    screen.blit(happyburgur, (self.x - self.width/2, self.y - self.height/2 + scschroael))
    pygame.display.set_caption("hifdgfgdfufggh score: " + str(round(self.hhiieeeiiieeostttcscohohrrroe, 0)))
burgurburgur = foodses("geinarick burgur", "foodz", 60,60 )
#print(burgurburgur.name)
burgurburgur.printInfo()
mcgrimise = foodses("simpl burgur", "burgurz", 60,60)
mcgrimise.printInfo()

# class burgurquein(): #platform
#   pass
# class mcronulds(): #player
#   def __init__(self):
#     self.image = burgurburger
gggjeiaimei = llllllllllllllleeeeeeeeeeeeeeevvvvvvvvvvvvvvvvvveeeeeeeeeeeeeeeelllllllllllllll(20, 0, 0)
alaibivvblbvievhvhfhfhihvibie = True

lagpic = False
running = True
while True:
  while alaibivvblbvievhvhfhfhihvibie:
    #input("mcchien: self.y")
    
    burgurburgur.update(gggjeiaimei.patforms)
    
    #print ("egg")
    gggjeiaimei.update(burgurburgur)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          burgurburgur.jump(gggjeiaimei.patforms)
          #hashtag both of these below it
    if lagpic == False:
      screen.fill("#eed8ae")
    if (600 - scschroael < burgurburgur.y - burgurburgur.height/2) :
      steveburnstetetxxtxt = open("scscscscororrrieieee.txt", "r").read()
      
      if steveburnstetetxxtxt == "" or float(steveburnstetetxxtxt) < burgurburgur.hhiieeeiiieeostttcscohohrrroe:
        file_obj = open("scscscscororrrieieee.txt", "w")
        file_obj.write(str(burgurburgur.hhiieeeiiieeostttcscohohrrroe))
        file_obj.close()
        text = font.render('hgihigighduhguirdscoere:' + str(round(burgurburgur.hhiieeeiiieeostttcscohohrrroe, 0)), True, (252, 3, 232), (238,216,174))
      alaibivvblbvievhvhfhfhihvibie = False
    screen.blit(text, text.get_rect())

  #mcchien
  pygame.display.update()
  screen.fill("#000000")

  #text1 restart burgur
  text1 = font.render('restart burgur jup', True, (252, 3, 232), (238,216,174))
  restart = pygame.Rect(300-100, 300-60, text1.get_width(), 120)
  pygame.draw.rect(screen,"#eed8ae", restart)
  screen.blit(text1, (200, 300-text1.get_height()/2))
 
        # alaibivvblbvievhvhfhfhihvibie = True aaaaaaaaaaaaaaaajoshua
  #text2 secret lore cool button really secret not obvious lore hidden button  and yes burgur lore is very secret so this button was hidden very well by the best burgur jump player ever and the lore is really secret really cool burgur burgur yes lore hidden secret lore hiding lore mysterious button also do not click or else bad things will happen i might be kidding with this but still beware of the hidden lore about hidden secret mysterious lore about burgur button a wise burgur once said that burgur lore was very secret and that he created all the burgurs in the world and that if you eat burgurs then the wise burgur will get mad for eating his creations and he will come after you and eat you alive so beware of the wise burgur that created all of the mysterious secret hidden burgur kind and also this hidden button so this lore is very secret and beware of everything i have told you this is all real totally real no fake no cap 100% real so please remember this message about the mysterious hidden secret button lore and about the legend of the wise burgur that created all of burgur kind so yes this lore is very cool very secret and all of the best burgurs will burgurgur you and they will eat you alive a second time until your entire body will dissolve in the burgurs stomach and the wise burgur will be happy that you have been deded for eating and disrespecting all the burgurs so yes do not be rude and disrespectful to the burgurs and if you are nice they will respect you 
  text2 = font.render('rugrub', True, (252, 3, 232),   (238,216,174))
  screen.blit(text2, text2.get_rect())
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      if restart.collidepoint(pos):
        print("live")
        alaibivvblbvievhvhfhfhihvibie = True
        burgurburgur.y = 500
        burgurburgur.x = 300
        scschroael = 0
        burgurburgur.dy = 0
        burgurburgur.dx = 0
        gggjeiaimei.numPatforms = 20
        gggjeiaimei.generatedhorse = 0
        gggjeiaimei.patforms = []
        for i in gggjeiaimei.gggggggggggggrrrrirnouoyernnnotyierrruubnoqd:
          gggjeiaimei.patforms.append(i)
        gggjeiaimei.gjeoineoratie()
        print(len(gggjeiaimei.patforms))
        print("h")
        burgurburgur.hhiieeeiiieeostttcscohohrrroe = 0  
      if text2.get_rect().collidepoint(pos):
        print("Lag commence")
        lagpic = True