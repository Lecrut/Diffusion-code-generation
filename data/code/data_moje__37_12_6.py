class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)):
            raise ValueError("Base must be a number")
        if not isinstance(height, (int, float)):
            raise ValueError("Height must be a number")
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    shape = Parallelogram(10, 5)
    print(shape.calculate_area())