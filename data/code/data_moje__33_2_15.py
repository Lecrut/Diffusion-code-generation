HALF = 0.5

class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return HALF * self.base * self.height

if __name__ == '__main__':
    shape = Triangle(12.0, 6.0)
    print(shape.get_area())