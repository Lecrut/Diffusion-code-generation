class Parallelogram:
    BASE: float = 12
    HEIGHT: float = 6

    def __init__(self, base: float = BASE, height: float = HEIGHT) -> None:
        self.base = base
        self.height = height

    def compute_area(self) -> float:
        return self.base * self.height

    def compute_perimeter(self, side_length: float) -> float:
        return 2 * (self.base + side_length)

if __name__ == '__main__':
    instance = Parallelogram()
    area_result = instance.compute_area()
    perimeter_result = instance.compute_perimeter(8)
    print(area_result)
    print(perimeter_result)