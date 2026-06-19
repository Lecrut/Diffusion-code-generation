from typing import ClassVar

class Triangle:
    MIN_SIDE_LENGTH: ClassVar[float] = 0.1

    def __init__(self, side_a: float, side_b: float, side_c: float):
        if not (Triangle.MIN_SIDE_LENGTH <= side_a <= side_b + side_c and Triangle.MIN_SIDE_LENGTH <= side_b <= side_a + side_c and (Triangle.MIN_SIDE_LENGTH <= side_c <= side_a + side_b)):
            raise ValueError('Invalid triangle sides')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    a_val = 3.0
    b_val = 4.0
    c_val = 5.0
    triangle = Triangle(a_val, b_val, c_val)
    print(triangle.perimeter())