import pgzrun
import random
WIDTH = 700
HEIGHT = 574
#################Scorea##################
total_score = 0
strength = 0
strength_submitted = False
wisdom = 0
wisdom_submitted = False
wisdom_collect = False
charm = 0
charm_submitted = False
charm_collect = False
mission1_start = False
random_total_score = 0
randomint = random.randint(-10,5)
credits = False
#################Aliens####################
alien = Actor('wizard')
alien.pos = 500, 500


dragon_running = Actor('dragon_running')
dragon_running.pos =500,300

dragon_firing = Actor('dragon_firing')
dragon_firing.pos =500,300

ok_dragon = Actor('ok_dragon')
ok_dragon.pos = 500, 300

music.play('main')
############Scenes#############################
scene1 = True
scene2 = False
scene3 = False
bar_fight = False
wizard_text1 = True
wizard_text2 = False
wizard_text3 = False

###############Scene Functions#####################
def draw_scene1():
    #music.play_once('tada')
    screen.blit('bgimage', (0,0))
    screen.draw.text("This is your\n  WarZone", (195, 200), fontname="freedom", fontsize=45)
    screen.blit('startbutton', (275, 300))
    screen.draw.text("Press enter to get started", (220, 425), fontname="start", fontsize=20,  color="#f07900", shadow=(2,2), scolor="#202020")
    
def draw_scene2():
    global total_score
    screen.blit('scene2', (0,0))
    alien.draw()
    #catching wizard when he stops for reference look at update function
    if total_score == 0:
        if alien.y <= 250:
            #text that wizard speaks
            screen.blit('thinking', (425,10))
            screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
            # screen.draw.text("Your mission\n is to save\n the planet", (515, 80), color="black")
            screen.draw.text("Press S to increase\n your score!\nor Enter to fight\n  the Dragon", (480, 110), color="black")
    elif total_score != 0:
        if alien.y <= 250:
            #text that wizard speaks
            screen.blit('thinking', (425,10))
            screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
            if total_score < 15:
                 screen.draw.text("Bad Intervention\n S to train more!\nor Enter to fight\n  the Dragon", (480, 110), color="black")
            elif total_score >= 15 and total_score < 24:
                screen.draw.text("Barely Alive!\n S to train more!\nor Enter to fight\n  the Dragon", (480, 110), color="black")
            elif total_score >= 24 :
                screen.draw.text("Good Intervention!\nReady to fight Dragon\nPress Enter", (480, 110), color="black")
def draw_scene3():
    global total_score 
    music.pause()
    screen.clear()
    screen.blit('dragon_background', (0,0))
    
    if total_score < 15 or total_score == 0:
       
        sounds.lost.play()
        screen.draw.text("Your total score was: " + str(total_score) + "\nYou lost!" "\nHa-Ha-Ha", (250, 80), color="white", fontsize=35)
        screen.draw.text('Press Enter ', (250,160), fontsize=35,  color='red')
        dragon_firing.draw()
        screen.blit('falling', (200,350))
        
    elif total_score >= 15 and total_score < 24:
        screen.draw.text('Press Enter ', (150,160), fontsize=35,  color='red')
        sounds.lost.play()
        
        screen.draw.text("Your total score was: " + str(total_score) + "\nDraw! " "\nGo Home!", (150, 15), color="white", fontsize=35, )
        ok_dragon.draw()
        screen.blit('feeling_ok', (50,260))
    elif total_score >= 24 :
        sounds.win.play()
        
        screen.draw.text('Press Enter ', (120,160), fontsize=35,  color='red')
        screen.draw.text("Your total score was: " + str(total_score) + "\nYou won!" "\nMission Completed!", (150, 15), color="white", fontsize=35, )
        dragon_running.draw()
        screen.blit('feeling_won', (50,260))
        
    
    
def draw_bar_fight():
    global strength
    global strength_submitted
    global total_score
    global wisdom_submitted
    global wisdom_collect
    screen.clear()
    screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
    screen.blit('innocent_big', (250, 100))
    screen.draw.text("Give me strength\n in the scale of 1 to 9!", (215, 50), color="white",  fontsize=35)
    if strength_submitted ==  True:
        screen.clear()
        screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
        screen.draw.text("Strength: " + str(strength), (20, 50), color="white", fontsize=35)
        screen.draw.text("All right All right,\nNow, give me some of your wisdom\nif you have any?\npress Enter", (215, 50), color="white",  fontsize=35)
        screen.blit('claiming_big', (250, 100))
        
def draw_wisdom():
    screen.clear()
    screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
    screen.draw.text("Strength: " + str(strength), (20, 50), color="white", fontsize=35)
    screen.blit('asking_wisdom_big', (250, 100))
    screen.draw.text("Give me wisdom\n in the scale of 1 to 9!", (215, 50), color="white",  fontsize=35)
    if wisdom_submitted ==  True:
        screen.clear()
        screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
        screen.draw.text("Strength: " + str(strength), (20, 50), color="white", fontsize=35)
        screen.draw.text("Wisdom: " + str(wisdom), (20, 80), color="white", fontsize=35)
        screen.draw.text("I am ready,\nto save the Planet\npress Enter to Start the mission", (215, 50), color="white",  fontsize=35)
        screen.blit('ready_big', (250, 100))

def draw_charm():
    

    
    screen.clear()
    screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
    screen.draw.text("Strength: " + str(strength), (20, 50), color="white", fontsize=35)
    screen.draw.text("Wisdom: " + str(wisdom), (20, 80), color="white", fontsize=35)
    screen.blit('asking_charm_big', (250, 100))
    screen.draw.text("I can not save the world without charm\n I need charm between 1 and 9!", (215, 50), color="white",  fontsize=35)
    if charm_submitted ==  True:
        screen.clear()
        screen.draw.text("Score: " + str(total_score), (20, 20), color="white", fontsize=35)
        screen.draw.text("Strength: " + str(strength), (20, 50), color="white", fontsize=35)
        screen.draw.text("Wisdom: " + str(wisdom), (20, 80), color="white", fontsize=35)
        screen.draw.text("Charm: " + str(charm), (20, 110), color="white", fontsize=35)
        screen.draw.text("Now ready,\npress Enter and get started", (215, 50), color="white",  fontsize=35)
        screen.blit('go_mission_big', (250, 100))
    
def draw_mission1():
    
    global random_total_score
    screen.clear()
    screen.blit('town', (0,0))
    ######
    screen.draw.text("Score: " + str(total_score)+ " " + 'Strength: '+ str(strength) + " " +  'Wisdom: ' + str(wisdom) + " " +  'Charm: ' + str(charm), (20, 20), color="black", fontsize=35)
    
    ########
    screen.blit('walking',(100,350))
    screen.blit('fighting_people',(400,350))
    screen.blit('thinking', (140,140))
    screen.draw.text("s to use strength and\n intervene\n   w to use wisdom\n   and c to use charm", (170, 225), color="black", fontsize=25)
    random_total_score = randomint + strength + charm + wisdom
    
def draw_credits():
      screen.clear()
      screen.draw.text('Developed by\n Sam Powers\nHamza Raza\nAkhmadillo Mamirov', (200,150), color="white", fontsize=35, fontname='start' )
      screen.draw.text('press r to restart the game', (190,350),color="orange", fontsize=25, fontname='start')
################## Conditions#########################
def on_key_up(key):
    global credits
    global scene1
    global scene2
    global scene3
    global strength
    global wisdom
    global bar_fight
    global strength_submitted
    global wisdom_submitted
    global wisdom_collect
    global charm_collect
    global charm
    global charm_submitted
    global mission1_start
    global total_score
    global random_total_score
    if key == keys.RETURN and scene1 == True:
        scene1 = False
        scene2 = True
        print('New Window')
    elif key == keys.RETURN and scene2 == True:
        scene2 = False
        scene3 = True
        print('Good good good')
    elif key == keys.S and scene2 == True:
        scene2 = False
        bar_fight = True
        print('Fight Scene Working')
    
    #Getting User Strength and saving it to a variable strength
    elif key == keys.K_0 and bar_fight:
        strength = 0
        strength_submitted = True
    elif key == keys.K_1 and bar_fight:
        strength = 1
        strength_submitted = True
    elif key == keys.K_2 and bar_fight:
        strength = 2
        strength_submitted = True
    elif key == keys.K_3 and bar_fight:
        strength = 3
        strength_submitted = True
    elif key == keys.K_4 and bar_fight:
        strength = 4
        strength_submitted = True
    elif key == keys.K_5 and bar_fight:
        strength = 5
        strength_submitted = True
    elif key == keys.K_6 and bar_fight:
        strength = 6
        strength_submitted = True
    elif key == keys.K_7 and bar_fight:
        strength = 7
        strength_submitted = True
    elif key == keys.K_8 and bar_fight:
        strength = 8
        strength_submitted = True
    elif key == keys.K_9 and bar_fight:
        strength = 9
        strength_submitted = True

    #Getting User Wisdom
    elif key == keys.RETURN and bar_fight and strength_submitted:
        bar_fight = False
        wisdom_collect = True

    elif key == keys.K_0 and wisdom_collect:
        wisdom = 0
        wisdom_submitted = True
    elif key == keys.K_1 and wisdom_collect:
        wisdom = 1
        wisdom_submitted = True
    elif key == keys.K_2 and wisdom_collect:
        wisdom = 2
        wisdom_submitted = True
    elif key == keys.K_3 and wisdom_collect:
        wisdom = 3
        wisdom_submitted = True
    elif key == keys.K_4 and wisdom_collect:
        wisdom = 4
        wisdom_submitted = True
    elif key == keys.K_5 and wisdom_collect:
        wisdom = 5
        wisdom_submitted = True
    elif key == keys.K_6 and wisdom_collect:
        wisdom = 6
        wisdom_submitted = True
    elif key == keys.K_7 and wisdom_collect:
        wisdom = 7
        wisdom_submitted = True
    elif key == keys.K_8 and wisdom_collect:
        wisdom = 8
        wisdom_submitted = True
    elif key == keys.K_9 and wisdom_collect:
        wisdom = 9
        wisdom_submitted = True
    #Gettin User Charm
    elif key == keys.RETURN and wisdom_collect  and wisdom_submitted:
        wisdom_collect =  False
        charm_collect = True
    elif key == keys.K_0 and charm_collect:
        charm = 0
        charm_submitted = True
    elif key == keys.K_1 and charm_collect:
        charm = 1
        charm_submitted = True
    elif key == keys.K_2 and charm_collect:
        charm = 2
        charm_submitted = True
    elif key == keys.K_3 and charm_collect:
        charm = 3
        charm_submitted = True
    elif key == keys.K_4 and charm_collect:
        charm = 4
        charm_submitted = True
    elif key == keys.K_5 and charm_collect:
        charm = 5
        charm_submitted = True
    elif key == keys.K_6 and charm_collect:
        charm = 6
        charm_submitted = True
    elif key == keys.K_7 and charm_collect:
        charm = 7
        charm_submitted = True
    elif key == keys.K_8 and charm_collect:
        charm = 8
        charm_submitted = True
    elif key == keys.K_9 and charm_collect:
        charm = 9
        charm_submitted = True
    
    elif key == keys.RETURN and charm_collect and charm_submitted:
        charm_collect = False
        mission1_start = True

    #taking back to scene 2
    elif key == keys.S and mission1_start:
        mission1_start = False
        scene2 = True
        total_score = random_total_score
    elif key == keys.W and mission1_start:
        mission1_start = False
        scene2 = True
        total_score = random_total_score
    elif key == keys.C and mission1_start:
        mission1_start = False
        scene2 = True
        total_score = random_total_score

    elif key== keys.RETURN and scene3:
        scene3 = False
        credits = True

    elif key==key.R and credits:
        strength_submitted = False
        wisdom_submitted = False
        charm_submitted = False
        credits = False
        total_score = 0
        scene1 = True
        strength = 0
        charm = 0 
        wisdom = 0
        sounds.win.stop()
        music.play('main')

    

        

        #credits  
def update():
    if scene2:
        if alien.y > 250:
            alien.x -=1.5
            alien.y -= 2
    

    

def draw():
    if scene1:
        draw_scene1()
    elif scene2:
        draw_scene2()
    elif scene3:
        draw_scene3()
    elif bar_fight:
        draw_bar_fight()
    elif wisdom_collect:
        draw_wisdom()
    elif charm_collect:
        draw_charm()
    elif mission1_start:
        draw_mission1()
    elif credits:
        draw_credits()
    
        
    


            

    
        
    


pgzrun.go()
