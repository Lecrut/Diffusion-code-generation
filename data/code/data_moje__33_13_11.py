from typing import Tuple

BASE_SCALE: float = 0.5

class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height * BASE_SCALE

    def dimensions(self) -> Tuple[float, float]:
        return (self.base, self.height)

if __name__ == '__main__':
    sample_base = 15
    sample_height = 8
    triangle_instance = Triangle(sample_base, sample_height)
    print(triangle_instance.area())
    print(triangle_instance.dimensions())