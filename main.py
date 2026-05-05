import pygame_easy as ge
import click

frame_index = 0
timer = 0
frame_index2 = 0
timer2 = 0
last_mode = None
move_stuff = None
able_to_move = True
current_song = None

def SpawnAsset(asset_sprite, x, y, scale, tag="tag"):
    return ge.Sprite(asset_sprite, x, y, scale, tag)
def CycleAnimations(frames, speed=0.1):
    global frame_index, timer
    timer += ge.delta_time()
    if timer >= speed:
        timer = 0
        frame_index = (frame_index + 1) % len(frames)
        ralsei.set_image(frames[frame_index])
def CycleAnimations2(frames, speed=0.1):
    global frame_index2, timer2
    timer2 += ge.delta_time()
    if timer2 >= speed:
        timer2 = 0
        frame_index2 = (frame_index2 + 1) % len(frames)
        dummy_ralsei.set_image(frames[frame_index2])

ge.init('Ralsei the Dark Prince', width=500, height=500, fps=30)
click.clear()
ge.play_music(r'Assets\Castle Town\town.mp3', loop=True, volume=1)
walk_down_sprite = [
    r"Animations/Walk down/walk_down_1.png",
    r"Animations/Walk down/walk_down_2.png",
    r"Animations/Walk down/walk_down_3.png",
    r"Animations/Walk down/walk_down_4.png"
]
walk_up_sprite = [
    r"Animations/Walk up/walk_up_1.png",
    r"Animations/Walk up/walk_up_2.png",
    r"Animations/Walk up/walk_up_3.png",
    r"Animations/Walk up/walk_up_4.png"
]
walk_right_sprite = [
    r"Animations/Walk right/walk_right_1.png",
    r"Animations/Walk right/walk_right_2.png",
    r"Animations/Walk right/walk_right_3.png",
    r"Animations/Walk right/walk_right_4.png"
]
walk_left_sprite = [
    r"Animations/Walk left/walk_left_1.png",
    r"Animations/Walk left/walk_left_2.png",
    r"Animations/Walk left/walk_left_3.png",
    r"Animations/Walk left/walk_left_4.png"
]
jump_sprite = [
    r"Animations/Jump/jump_1.png",
    r"Animations/Jump/jump_2.png",
    r"Animations/Jump/jump_3.png",
    r"Animations/Jump/jump_4.png",
    r"Animations/Jump/jump_5.png",
    r"Animations/Jump/jump_6.png",
    r"Animations/Jump/jump_7.png",
    r"Animations/Jump/jump_8.png",
    r"Animations/Jump/jump_9.png",
    r"Animations/Jump/jump_10.png",
    r"Animations/Jump/jump_11.png"
]
hug_sprite = [
    r"Animations/Hug/hug_2.png",
    r"Animations/Hug/hug_3.png",
    r"Animations/Hug/hug_4.png"
]
dance_sprite = [
    r"Animations/Dance/dance_1.png",
    r"Animations/Dance/dance_2.png",
    r"Animations/Dance/dance_3.png",
    r"Animations/Dance/dance_4.png",
    r"Animations/Dance/dance_5.png",
    r"Animations/Dance/dance_6.png",
    r"Animations/Dance/dance_7.png",
    r"Animations/Dance/dance_8.png"
]
dummy_dance = [
    r'Assets\Dummy Ralsei\dummy_1.png',
    r'Assets\Dummy Ralsei\dummy_2.png',
    r'Assets\Dummy Ralsei\dummy_3.png',
    r'Assets\Dummy Ralsei\dummy_4.png'
]
dummy_blush = [
    r'Assets\Dummy Ralsei\dummy_blush_1.png',
    r'Assets\Dummy Ralsei\dummy_blush_2.png',
    r'Assets\Dummy Ralsei\dummy_blush_3.png',
    r'Assets\Dummy Ralsei\dummy_blush_4.png'
]
wall_1_1 = SpawnAsset(r'Assets\Wall 1\wall_2.png', 0, 50, 0.6)
wall_1_2 = SpawnAsset(r'Assets\Wall 1\wall_1.png', 220, 50, 0.6)
wall_2_1 = SpawnAsset(r'Assets\Wall 2\wall.png', -50, 0, scale=5, tag="wall")
wall_2_2 = SpawnAsset(r'Assets\Wall 2\wall.png', 450, 0, scale=20, tag="wall")
wall_1_3 = SpawnAsset(r'Assets\Wall 1\wall_2.png', 295, 440, 0.6)
wall_1_4 = SpawnAsset(r'Assets\Wall 1\wall_1.png', -179, 440, 0.6)
ground = SpawnAsset(r'Assets\Floor\ground.png', -102, -10, scale=1.1, tag="ground")
dummy_ralsei = SpawnAsset(r'Assets\Dummy Ralsei\dummy_idle.png', 300, 250, scale=2.1, tag='dummy')
ralsei = ge.Sprite(walk_down_sprite[0], x=250, y=250, scale=2)
def update():
    global move_stuff
    global last_mode
    global able_to_move
    global current_song
    move_stuff = False
    if ralsei.collides_with(wall_1_1) or ralsei.collides_with(wall_1_2):
        able_to_move = False
        ralsei.y += 2
    elif ralsei.collides_with(wall_1_3) or ralsei.collides_with(wall_1_4):
        able_to_move = False
        ralsei.y -= 2
    elif ralsei.collides_with(wall_2_1):
        able_to_move = False
        ralsei.x += 2
    elif ralsei.collides_with(wall_2_2):
        able_to_move = False
        ralsei.x -= 2
    else:
        able_to_move = True
    if able_to_move == True:
        if ge.key_held('down'):
            ralsei.y += 4
            last_mode = 'down'
            move_stuff = True
        if ge.key_held('up'):
            ralsei.y -= 4
            last_mode = 'up'
            move_stuff = True
        if ge.key_held('right'):
            ralsei.x += 4
            last_mode = 'right'
            move_stuff = True
        if ge.key_held('left'):
            ralsei.x -= 4
            last_mode = 'left'
            move_stuff = True
        if ge.key_pressed('escape'):
            click.clear()
            ge.quit_game()
        if ge.key_held('d'):
            last_mode = 'dance'
            move_stuff = True
        elif ge.key_released('d'):
            move_stuff = False
            ralsei.set_image(r'Animations\Walk down\walk_down_1.png')
        if ge.key_held('h'):
            last_mode = 'hug'
            move_stuff = True
        if move_stuff:
            if last_mode == 'dance':
                CycleAnimations(dance_sprite, speed=0.2)
            elif last_mode == 'hug':
                CycleAnimations(hug_sprite, speed=0.2)
            elif last_mode == 'up':
                CycleAnimations(walk_up_sprite, speed=0.2)
            elif last_mode == 'down':
                CycleAnimations(walk_down_sprite, speed=0.2)
            elif last_mode == 'left':
                CycleAnimations(walk_left_sprite, speed=0.2)
            elif last_mode == 'right':
                CycleAnimations(walk_right_sprite, speed=0.2)
        else:
            if last_mode == 'up':
                ralsei.set_image(walk_up_sprite[0])
            elif last_mode == 'down':
                ralsei.set_image(walk_down_sprite[0])
            elif last_mode == 'right':
                ralsei.set_image(walk_right_sprite[0])
            elif last_mode == 'left':
                ralsei.set_image(walk_left_sprite[0])
        if last_mode == 'dance' and current_song != 'funk':
            ge.play_music(r'Assets\Diversion\beats.mp3', loop=True, volume=0.7)
            current_song = 'funk'
        elif last_mode != 'dance' and current_song != 'normal':
            ge.play_music(r'Assets\Castle Town\town.mp3', loop=True, volume=0.7)
            current_song = 'normal'
        if last_mode == 'dance':
            CycleAnimations2(dummy_dance, speed=0.2)
        elif last_mode == 'hug' and ralsei.collides_with(dummy_ralsei):
            CycleAnimations2(dummy_blush, speed=0.2)
ge.run(update_fn=update)