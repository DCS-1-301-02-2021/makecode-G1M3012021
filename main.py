scene.set_background_color(8)
spacePlane=sprites.create(img("""
    . . . . . . . . . . . . . . . .
    8 8 8 8 8 . . . . . . . . . . .
    8 8 8 8 8 . . . . . . . . . . .
    2 2 . . . . . . . . . . . . . .
    2 4 f f . . . . . . . . . . . .
    2 4 f f f f f f 5 . . . . . . .
    2 2 . f f f 5 5 5 2 2 2 2 2 2 .
    . . . f f f 5 f f 2 f f f 2 2 .
    . . . f f f f f f f f f f 2 2 .
    2 2 . f f f f f f f f f f . . .
    2 4 f f . . . . . . . . . . . .
    2 4 f f . . . . . . . . . . . .
    2 2 . . . . . . . . . . . . . .
    8 8 8 8 8 . . . . . . . . . . .
    8 8 8 8 8 . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.player)
info.set_life(3)
spacePlane.set_stay_in_screen(True)
controller.move_sprite(spacePlane,200,200)
def on_a_pressed():
    missile=sprites.create_projectile_from_sprite(
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . a . . . .
            . . . . . . . . . a a a a a . .
            . . . . . . . . . a a a a a . .
            . . . . . . . . a a a a a a a .
            . . . . a a . . a a a a a a a .
            . . . . . a . . a a a a a a a .
            . . . . . a . . . a a a a a . .
            a a a a a a a a a a a a a a a 2
            . . . . . a . . . a a a a a . .
            . . . . . a . . a a a a a a a .
            . . . . . a . . a a a a a a a .
            . . . . a a . . a a a a a a a .
            . . . . . . . . a a a a a a a .
            . . . . . . . . . a a a a a . .
            . . . . . . . . . . . a . . . .
        """), spacePlane, 200,0)
controller.A.on_event(
    ControllerButtonEvent.PRESSED, on_a_pressed
)

def on_update():
    bogy=sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . 2 2 . . .
        . . f f f f f f f f f 5 2 2 . .
        . f 5 1 f f f f f f f 5 2 2 2 .
        f f f f f f f f f f f 5 2 2 2 1
        f 1 1 1 1 f f f f f f 5 2 2 2 1
        f 2 2 2 1 f f f f f f 5 2 2 2 1
        . f 2 2 1 f f f f f f 5 2 2 2 .
        . . f f f f f f f f f 5 2 2 . .
        . . . . . . . . . . . 2 2 . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
        SpriteKind.enemy)
    bogy.set_velocity(-100,randint(-30,30))
    bogy.y=randint(0,scene.screen_height())
    bogy.left=scene.screen_width()
    bogy.set_flag(SpriteFlag.AUTO_DESTROY,True)
game.on_update_interval(500, on_update)

def on_hit(sprite, othersprite):
    othersprite.destroy(effects.fire,100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, 
    SpriteKind.enemy,on_hit)

def on_crash(sprite,othersprite):
    othersprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.enemy,on_crash)