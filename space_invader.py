import pygame

# creating a game window (that is) initialize pi game to access the code methods in py game module
# First important step is to initialize pi game [Must step to make our game work]
pygame.init()

# Step 2: create a screen for our game
# TIL : display -> Setting the display mode in pygame creates a visible image surface on the monitor.
# This surface can either cover the full screen, or be windowed on platforms that support a window
# manager. The display surface is nothing more than a standard pygame surface object. There are special functions
# needed in the pygame.display pygame module to control the display window and screen module to keep the image surface
# contents updated on the monitor.

# set_mode(tuple(width, height), flags, display, vsync) -> This function will create a display Surface.
# there are number ways to initialise the display screen .
screen = pygame.display.set_mode((800, 600))

# Event -> anything happens in our game window like closing the game is quit game, moving the mouse up and down
# everything inside a game window is event

# To create a game loop -> we passed a switch variable as a running to make the game window
running = True

while running:
    # create a for loop and create a variable event pygame events -> Pygame handles all its event messaging through
    # an event queue. The input queue is heavily dependent on the pygame. display pygame module to control the
    # display window and screen module. If the display has not been initialized and a video mode not set,
    # the event queue may not work properly.

    # pygame.event.get() -> This will get all the messages and remove them from the queue. If a type or sequence
    # of types is given only those messages will be removed from the queue and returned.
    for event in pygame.event.get():

        # QUIT = quit the game and turn running to False
        if event.type == pygame.QUIT:
            running = False

