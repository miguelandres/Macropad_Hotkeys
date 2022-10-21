# MACROPAD Hotkeys: Zoom Hotkeys

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from action import MediaControl

app = {
    'name': 'Zoom',
    'order': 1,
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.A]),
        (0x544408, 'Screen ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.S]),
        (0x04541B, 'Video  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.V]),
        # 2nd row ----------
        (0x000754, 'Control', [Keycode.CONTROL,
         Keycode.OPTION, Keycode.COMMAND, Keycode.H]),
        (0x000000, '       ', []),
        (0x000754, 'Leave  ', [Keycode.COMMAND, Keycode.W]),
        # 3rd row ----------
        (0x000000, '       ', []),
        (0x095E06, 'Play/Pause',
         [MediaControl(ConsumerControlCode.PLAY_PAUSE)]),
        (0x000000, '       ', []),
        # 4th row ----------
        (0x080F54, 'Vol-   ',
         [MediaControl(ConsumerControlCode.VOLUME_DECREMENT)]),
        (0x000000, '       ', []),
        (0x080F54, 'Vol+   ',
         [MediaControl(ConsumerControlCode.VOLUME_INCREMENT)])
    ]
}
