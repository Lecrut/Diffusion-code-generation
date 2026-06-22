import operator

class Parallelogram:
    def __init__(self, base, height):
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.base = base
        self.height = height

    def calculate_area(self):
        return operator.mul(self.base, self.height)

if __name__ == '__main__':
    shape = Parallelogram(7.5, 12)
    print(shape.calculate_area())