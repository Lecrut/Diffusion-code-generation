class Triangle:

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    side1_length = 6.0
    side2_length = 8.0
    side3_length = 10.0
    triangle_instance = Triangle(side1_length, side2_length, side3_length)
    calculated_perimeter = triangle_instance.perimeter()
    print(calculated_perimeter)