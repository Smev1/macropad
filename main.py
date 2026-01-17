from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# --------------------
# Direct pin wiring
# --------------------
keyboard.coord_mapping = [
    0, 1, 2,
    3, 4, 5,
    6, 7
]

keyboard.direct_pins = [
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP6,
    board.GP29,
    board.GP28,
    board.GP27
]

keyboard.col_pins = ()
keyboard.row_pins = ()

# --------------------
# RGB (SK6812 / NeoPixel)
# --------------------
rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=6,
    val_limit=100,
    animation_mode=RGB.RAINBOW,
)

keyboard.extensions.append(rgb)

# --------------------
# Keymap
# --------------------
keyboard.keymap = [
    [
        KC.COPY,   KC.PASTE, KC.CUT,
        KC.UNDO,   KC.REDO,  KC.ENTER,
    ]
]

if __name__ == '__main__':
    keyboard.go()
