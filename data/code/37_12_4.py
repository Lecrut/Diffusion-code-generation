class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numeric values.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    parallelogram = Parallelogram(base=10, height=5)
    area = parallelogram.calculate_area()
    print(area)