class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self._calculate_perimeter()

    def _calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    side_a = 6
    side_b = 8
    side_c = 10
    triangle_instance = Triangle(side_a, side_b, side_c)
    result = triangle_instance.perimeter()
    print(result)