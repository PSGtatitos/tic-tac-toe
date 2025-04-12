import pygame
from sys import exit

pygame.init()

shapes = []
screen = pygame.display.set_mode((400,400))
screen.fill(color="white")
pygame.display.set_caption("tic tac toe")

board_surface = pygame.image.load("graphics/tic-tac-toe.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if event.button == 1:  # Left click
                shapes.append(('circle', pos))
            elif event.button == 3:  # Right click
                shapes.append(('x', pos))
    screen.blit(board_surface,(0,0))
    for shape, pos in shapes:
        if shape == 'circle':
            pygame.draw.circle(screen, (0, 0, 255), pos, 20)  # Blue circle
        elif shape == 'x':
            x, y = pos
            size = 20
            
            pygame.draw.line(screen, (255, 0, 0), (x - size, y - size), (x + size, y + size), 3)
            pygame.draw.line(screen, (255, 0, 0), (x - size, y + size), (x + size, y - size), 3)
            
        
    pygame.display.update()