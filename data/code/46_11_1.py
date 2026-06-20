from typing import Union

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    triangle = Triangle(3.0, 4.0, 5.0)
    print(triangle.perimeter())