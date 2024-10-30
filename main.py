def on_gesture_shake():
    if True:
        for index in range(9999):
            music.play(music.string_playable("B - B - B - B - ", 156),
                music.PlaybackMode.UNTIL_DONE)
        for index2 in range(9999):
            basic.show_leds("""
                . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
                """)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

datalogger.log(datalogger.create_cv("9", 0), datalogger.create_cv("1", 0))

def on_forever():
    pass
basic.forever(on_forever)
