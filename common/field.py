from vector import Vector

FIELD_CENTERED = True

class Field:
    def __init__(self, size):
        """
        size - tuple containing horizontal and vertical size of field
        """
        self.size = size
        if FIELD_CENTERED:
            self.left = -0.5 * size[0]
            self.bottom = -0.5 * size[1]
            self.right = 0.5 * size[0]
            self.top = 0.5 * size[1]
        else:
            self.left = 0
            self.bottom = 0
            self.right = size[0]
            self.top = size[1]
        self.width = self.right - self.left
        self.height = self.top - self.bottom


    def fit_in_rect(self, pos, resolution):
        rl = 0
        rw = resolution[0]
        rb = 0
        rh = resolution[1]
        return Vector(int(rl + rw * (pos.x - self.left) / self.width),
                      int(rb + rh * (1.0 - (pos.y - self.bottom) / self.height)))

