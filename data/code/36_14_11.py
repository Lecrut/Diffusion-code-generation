class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0:
            raise ValueError("base1 must be positive")
        if base2 <= 0:
            raise ValueError("base2 must be positive")
        if height <= 0:
            raise ValueError("height must be positive")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2.0

if __name__ == '__main__':
    trap = Trapezoid(4.0, 6.0, 8.0)
    print(trap.area())