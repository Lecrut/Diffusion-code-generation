class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self._pi = 3.14159265358979323846
        self._third = 1.0 / 3.0

    def base_area(self):
        return self._pi * (self.radius ** 2)

    def volume(self):
        return self._third * self.base_area() * self.height

if __name__ == '__main__':
    c = Cone(radius=7, height=5)
    print(c.base_area())
    print(c.volume())