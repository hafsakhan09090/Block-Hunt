import pygame
import random 

pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Block Hunt <3") 
clock=pygame.time.Clock()

a_x=200
a_y = 150
a_speed=7
b_x=100 
b_y = 100
score=0 

start_time=pygame.time.get_ticks() 
game_time=60000
time_left=60 

TEAL=(0,255,0) 
CYAN = (0,255,255) 
LIME_YELLOW=(204,255,0) 
CHERRY_RED=(210, 4, 45)
NEON_PINK=(251, 72, 196)

font=pygame.font.SysFont("Dina",50) 
big_font=pygame.font.SysFont("Hack",70) 

running=True
game_over=False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
    
    if game_over==False:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]==True:
            a_x=a_x-a_speed 
        if keys[pygame.K_RIGHT]==True:
            a_x=a_x+a_speed
        if keys[pygame.K_UP]:
            a_y=a_y-a_speed 
        if keys[pygame.K_DOWN]:
            a_y=a_y+a_speed
        
        a_x=max(0,min(a_x,900-30)) 
        a_y=max(0,min(a_y,600-30))
        
        a_rect=pygame.Rect(a_x,a_y,30,30)
        b_rect=pygame.Rect(b_x,b_y,20,20)
        if a_rect.colliderect(b_rect):
            score=score+1
            b_x=random.randint(0,900-20) 
            b_y=random.randint(0,600-20)
    
    current_time=pygame.time.get_ticks()
    time_left=(game_time-(current_time-start_time))//1000 
    if time_left<=0:
        game_over=True 
        time_left=0 

    screen.fill((0,0,0)) 
    
    pygame.draw.rect(screen,TEAL,(a_x,a_y,30,30)) 
    pygame.draw.rect(screen,CYAN,(b_x,b_y,20,20)) 
    
    score_text=font.render(" Score: "+str(score),True,LIME_YELLOW)
    screen.blit(score_text,(20,20)) 
    timer_text=font.render("Time: "+str(time_left),True,CHERRY_RED)
    screen.blit(timer_text,(900-155,20)) 
    
    if game_over==True:
        final_text=big_font.render("You’ve got the score: "+str(score),True,NEON_PINK)
        screen.blit(final_text,(900//2-300,600//2))
    
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 