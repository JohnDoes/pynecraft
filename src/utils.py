"""src/utils.py"""
from direct.gui.DirectGui import *
from panda3d.core import *


class DrawImage(OnscreenImage):
    def __init__(self, parent=None, image=None, scale=(1, 1, 1), pos=(0, 0, 0)):
        super().__init__(
            parent=parent,
            image=image,
            pos=pos,
            scale=scale,
        )
        self.setName(image)
        self.setTransparency(TransparencyAttrib.M_alpha)


class DrawText(OnscreenText):
    def __init__(self, parent=None, text='', font=None, scale=0.07, pos=(0.05, -0.1), fg=(0, 0, 0, 1), bg=(0, 0, 0, 0.1)):
        super().__init__(
            parent=parent,
            text=text,
            align=TextNode.ALeft,
            pos=pos,
            scale=scale,
            font=font,
            fg=fg,
            bg=bg,
            mayChange=True,
        )
        self.start_time = None