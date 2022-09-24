# import the pygame module, so you can use it
import pygame

BLUE = (0, 0, 250)

background_path = 'background240x180.png'
background_pos = (0, 0)
logo_path = 'logo32x32.png'
face_path = 'face48x48.png'
face_pos_x = 50
face_pos_y = 50
step_x = 10
step_y = 10
caption_text = 'minimal program'
screen_size = screen_width, screen_height = (240, 180)

# define a main function
def main():
    # make global pos variables
    global face_pos_x, face_pos_y, step_x, step_y

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo_image = pygame.image.load(logo_path)
    pygame.display.set_icon(logo_image)
    pygame.display.set_caption(caption_text)

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode(screen_size)

    # load background
    background_image = pygame.image.load(background_path)
    # load face image
    face_image = pygame.image.load(face_path)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # fill the background
        screen.fill(BLUE)
        # blit the background image on the screen
        screen.blit(background_image, background_pos)
        # blit the face image on the screen
        screen.blit(face_image, (face_pos_x, face_pos_y))
        
        # refresh the screen
        pygame.display.flip()

        # calculate the face position with screen boundaries
        if face_pos_x>screen_width-48 or face_pos_x<0:
            step_x = -step_x
        if face_pos_y>screen_height-48 or face_pos_y<0:
            step_y = -step_y

        face_pos_x += step_x
        face_pos_y += step_y

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()