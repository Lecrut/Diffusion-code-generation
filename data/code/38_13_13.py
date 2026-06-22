import math

class Cone:
    def __init__(self, r: float, h: float):
        self.r = r
        self.h = h

    def volume(self) -> float:
        if self.r <= 0 or self.h <= 0:
            return 0.0
        return (math.pi * (self.r ** 2) * self.h) / 3

if __name__ == '__main__':
    c = Cone(3, 8)
    print(c.volume())