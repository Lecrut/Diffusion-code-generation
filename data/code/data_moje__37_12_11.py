class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

if __name__ == '__main__':
    para = Parallelogram(10, 5)
    print(para.area())