import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
largura, altura = 600, 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Define cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Configura o relógio para controlar o FPS
clock = pygame.time.Clock()

# Loop Principal
while True:
    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche o fundo com branco
    tela.fill(BRANCO)

    # Desenha um círculo azul no meio da tela
    pygame.draw.circle(tela, AZUL, (largura // 2, altura // 2), 50)

    # Atualiza a tela
    pygame.display.flip()

    # Controla o FPS
    clock.tick(60)
