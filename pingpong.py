from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, p_spd, width, h):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (width, h))
        self.speed = p_spd
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed

backgr = (200, 255, 255)
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
window.fill(backgr)

game = True
finnish = False
clock = time.Clock()
fps = 60

r_1 = Player('Stik.jpeg', 30, 200, 4, 50, 150)
r_2 = Player('Stik.jpeg', 520, 200, 4, 50, 150)
bol = GameSprite('Bol.jpeg', 200, 200, 4, 50, 50)
font.init()
font = font.Font(None, 35)
lose_1 = font.render('P2 won', True, (180, 0, 0))
lose_2 = font.render('P1 won', True, (180, 0, 0))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finnish != True:
        window.fill(backgr)
        r_1.update_l()
        r_2.update_r()
        bol.rect.x += speed_x
        bol.rect.y += speed_y
        if sprite.collide_rect(r_1, bol) or sprite.collide_rect(r_2, bol):
            speed_x *= -1
            speed_y *= 1

        if bol.rect.y > win_h - 50 or bol.rect.y < 0:
            speed_y *= -1
        if bol.rect.x < 0:
            finnish = True
            window.blit(lose_1, (200, 200))
            game_over = True
        if bol.rect.x > win_w:
            finnish = True
            window.blit(lose_2, (200, 200))
            game_over = True
        r_1.reset()
        r_2.reset()
        bol.reset()
    display.update()
    clock.tick(fps)