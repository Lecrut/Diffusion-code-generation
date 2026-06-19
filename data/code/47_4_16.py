class Triangle:

    def __init__(self, base, height):
        if not self._is_valid_base_height(base, height):
            raise ValueError('Base and height must be positive numbers.')
        self.base = base
        self.height = height

    @staticmethod
    def _is_valid_base_height(base, height):
        return base > 0 and height > 0

    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    try:
        triangle1 = Triangle(10, 5)
        area1 = triangle1.calculate_area()
        print(area1)
        triangle2 = Triangle(7, 3)
        area2 = triangle2.calculate_area()
        print(area2)
        invalid_triangle = Triangle(-1, 5)
    except ValueError as e:
        print(e)