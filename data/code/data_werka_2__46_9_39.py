from typing import Tuple

class Triangle:
    def __init__(self, sides: Tuple[float, float, float]):
        self.sides = sides

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = (7.0, 24.0, 25.0)
    triangle_instance = Triangle(triangle_sides)
    print(f"Perimeter of the triangle with sides {triangle_sides}: {triangle_instance.perimeter()}")