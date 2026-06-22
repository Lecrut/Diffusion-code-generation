class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self._sum_sides()

    def _sum_sides(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    first_side_length = 7.0
    second_side_length = 9.0
    third_side_length = 12.0
    triangle_instance = Triangle(first_side_length, second_side_length, third_side_length)
    result_perimeter = triangle_instance.perimeter()
    print(result_perimeter)