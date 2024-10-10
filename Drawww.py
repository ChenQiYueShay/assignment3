import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置画布大小和颜色
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Draw with Mouse")

# 设置画笔颜色和大小
draw_color = (0, 0, 0)
brush_size = 5

# 存储线条的栈
lines = []
current_line = []

# 主循环
drawing = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键按下
                drawing = True
                current_line = []
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 左键松开
                drawing = False
                if current_line:
                    lines.append(current_line)
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_x, mouse_y = event.pos
                pygame.draw.circle(screen, draw_color, (mouse_x, mouse_y), brush_size)
                current_line.append((mouse_x, mouse_y))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if lines:
                    lines.pop()
                    screen.fill((255, 255, 255))
                    for line in lines:
                        for point in line:
                            pygame.draw.circle(screen, draw_color, point, brush_size)

    pygame.display.flip()