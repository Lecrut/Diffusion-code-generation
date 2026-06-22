from typing import Tuple

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @staticmethod
    def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
        return (side_a > 0 and side_b > 0 and side_c > 0) and \
               (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a)

    def get_perimeter(self) -> float:
        if not self.is_valid_triangle(self._side_a, self._side_b, self._side_c):
            raise ValueError("Invalid triangle sides")
        return self._side_a + self._side_b + self._side_c

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (3.0, 4.0, 5.0)
    try:
        t = Triangle(*sample_sides)
        perimeter = t.get_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)