import pygame

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = (300,) * 2
    pygame.display.set_caption("Герой двигается!")
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("white"))

    fps = 60  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True

    all_sprites = pygame.sprite.Group()
    all_sprites.draw(screen)

    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                all_sprites.update(event)

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        pygame.display.flip()  # смена кадра
        # временная задержка
        clock.tick(fps)