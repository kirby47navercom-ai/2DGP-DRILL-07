from pico2d import *
import random

from sdl2.examples.pong import Ball


# Game object class here
class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += random.randint(-1, 2)

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
        self.x, self.y, frame_width // 2, frame_height // 2)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')



    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x = random.randint(600, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += random.randint(-2,1)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




def reset_world():
    global running
    running = True

    global world

    world = []
    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    ball = [Ball() for i in range(20)]



def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()
reset_world()
while running:
    handle_events()
    #게임 로직
    update_world()
    #게임 랜더링
    render_world()
    delay(0.02)

close_canvas()
