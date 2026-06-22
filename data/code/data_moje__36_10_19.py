class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def get_area(self):
        return (self.base1 + self.base2) * self.height / 2

if __name__ == '__main__':
    trapezoid = Trapezoid(5, 7, 4)
    area = trapezoid.get_area()
    print(area)