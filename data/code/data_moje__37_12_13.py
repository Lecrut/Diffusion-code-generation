class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numeric values.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    parallelogram = Parallelogram(10.0, 5.0)
    print(parallelogram.calculate_area())