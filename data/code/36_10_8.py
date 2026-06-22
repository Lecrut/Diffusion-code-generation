class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

if __name__ == '__main__':
    trapezoid = Trapezoid(5, 10, 4)
    result = trapezoid.area()
    print(result)