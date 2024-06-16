from pygame import * 
from random import * 
from time import time as timer 
 
win_width = 700 
win_height = 500 
 
mw = display.set_mode((win_width, win_height)) 
back = (255, 255, 255)
clock = time.Clock() 

 
mixer.init() 
font.init() 
 
 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y,size_x, size_y,player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
 
    def reset(self): 
        mw.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
class Player(GameSprite): 
    def update_r(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y< win_width - 70: 
            self.rect.y += self.speed 
    def update_l(self):
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y< win_width - 70: 
            self.rect.y += self.speed 

racket_l = Player('racket.png',10, 150,20,100,25)
racket_r = Player('racket.png',660, 180,40,100,25)
ball = GameSprite('ball.png', 330, 200,40,40,50)
 
speed_x = 3
speed_y = 3
finish = False 
game = True 
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if not finish:
        mw.fill(back)
        racket_l.update_l()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r,ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height - 40 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True

        if ball.rect.x > win_height:
            finish = True

        racket_l.reset()
        racket_r.reset()
        ball.reset()

    display.update()      
    clock.tick(40)