import pygame as pg
from pygame.locals import *
import os

SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 700
pg.init()
MENU_FONT = pg.font.SysFont('comicsans', 300)
OPTIONS_FONT = pg.font.SysFont('comicsans', 100)

RAT_IMAGE = pg.image.load(os.path.join('Assets', 'spr_rat_right.png'))

def draw_text(text, font, color, surface, x, y):
    draw_text = font.render(text, 1, color)
    if x == 8000:
        x = SCREEN_WIDTH//2 - draw_text.get_width()/2
    if y == 8000:
        y = SCREEN_HEIGHT//2 - draw_text.get_height()/2
    
    surface.blit(draw_text, (x, y))

def main_menu(surface):

    cursor_pos = 0

    while True:
        surface.fill((0,0,0))
        
        draw_text('MAIZE', MENU_FONT, (255,255,255), surface, 8000, 100)
        draw_text('PLAY GAME', OPTIONS_FONT, (255,255,255), surface, 8000, 350)
        draw_text('OPTIONS', OPTIONS_FONT, (255,255,255), surface, 8000, 450)
        draw_text('CREDITS', OPTIONS_FONT, (255,255,255), surface, 8000, 550)

        surface.blit(RAT_IMAGE, (250, cursor_pos*100 + 350))

        pg.display.update()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN and cursor_pos < 2:
                    cursor_pos += 1
                if event.key == pg.K_UP and cursor_pos > 0:
                    cursor_pos -= 1
                if event.key == pg.K_RETURN:
                    if cursor_pos == 0:
                        return 0
                    if cursor_pos == 2:
                        credits_menu(surface)
    
    return 0

def credits_menu(surface):

    while True:
        surface.fill((0,0,0))
        
        draw_text('Tail :D', MENU_FONT, (255,255,255), surface, 8000, 100)

        pg.display.update()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0