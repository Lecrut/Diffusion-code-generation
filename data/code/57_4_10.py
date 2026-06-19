class Parallelogram:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

if __name__ == '__main__':
    try:
        parallelogram = Parallelogram(base=10, height=5)
        print(parallelogram.area())
    except ValueError as e:
        print(e)