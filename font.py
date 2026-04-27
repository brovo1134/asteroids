import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Font(pygame.sprite.Sprite):
    def __init__(self, f_size=16):
        super().__init__(self.containers)
        self.font = pygame.font.SysFont(None, f_size)

    def draw(self, screen, text):
        img = self.font.render(text, True, "RED")
        screen.blit(img, (20, 20))
