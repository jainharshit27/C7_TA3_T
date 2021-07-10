import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

ground = pygame.image.load("sprites/ground.png")
ground_rect = pygame.Rect(0, 330, 1200, 2)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    image_width = ground.get_width()
    screen.blit(ground, ground_rect)
    screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
    ground_rect.x -= 1
    if ground_rect.x <= -image_width:
        screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
        ground_rect.x = 0

    pygame.display.update()