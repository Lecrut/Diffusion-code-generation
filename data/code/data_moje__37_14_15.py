class Parallelogram:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
        if self.base <= 0:
            raise ValueError("Base must be positive")
        if self.height <= 0:
            raise ValueError("Height must be positive")

    def area(self) -> float:
        return self.base * self.height

if __name__ == '__main__':
    BASE_VAL = 12.75
    HEIGHT_VAL = 8.3
    shape = Parallelogram(BASE_VAL, HEIGHT_VAL)
    print(shape.area())