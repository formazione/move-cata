import pygame


pygame.init()

screen = pygame.display.set_mode((600, 400)) # window
clock = pygame.time.Clock()
# PLAYER


# starting position of the player
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.pos = self.x, self.y
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.image  = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))

    def stop(self):
        ''' called when you key up and stops the player '''
        self.left, self.right, self.up, self.down = 0, 0, 0, 0

player = Player()

# Indicates where the player is directed
def get_key(event):
    ''' checks which key you pressed '''
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        return "left"
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        return "right"    
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        return "up".
        
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        return "down"


while True:
    if player.left:
        player.x -= 1
    elif player.right:
        player.x += 1
    elif player.up:
        player.y -= 1
    elif player.down:
        player.y += 1
    screen.fill(0)
    if pygame.event.get(pygame.QUIT):
        break
    # Movements... if press arrow keys...
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if get_key(event) == "left":
                player.left = 1
                player.right = 0
            elif get_key(event) == "right":
                player.right = 1
                player.left = 0            
            elif get_key(event) == "up":
                player.up = 1
                player.down = 0
            elif get_key(event) == "down":
                player.down = 1
                player.up = 0
        elif event.type == pygame.KEYUP:
            player.stop()
    screen.blit(player.image , (player.x, player.y))
    clock.tick(60)
    pygame.display.update()

pygame.quit()
'''The post:
https://pythonprogramming.altervista.org/how-to-move-the-player-with-pygame/ '''