class Trapezoid:
    def __init__(self, base1, base2, height):
        if height <= 0:
            raise ValueError("Height must be positive.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @property
    def base1(self):
        return self._base1

    @base1.setter
    def base1(self, value):
        if value <= 0:
            raise ValueError("Base1 must be positive.")
        self._base1 = value

    @property
    def base2(self):
        return self._base2

    @base2.setter
    def base2(self, value):
        if value <= 0:
            raise ValueError("Base2 must be positive.")
        self._base2 = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    trapezoid = Trapezoid(5, 7, 4)
    print(trapezoid.area())