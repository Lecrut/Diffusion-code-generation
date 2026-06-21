class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_inputs()

    def _validate_inputs(self):
        if self.base <= 0:
            raise ValueError('Base must be a positive number.')
        if self.height <= 0:
            raise ValueError('Height must be a positive number.')

    @property
    def area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    try:
        triangle1 = Triangle(10, 5)
        print(triangle1.area)
    except ValueError as e:
        print(e)
    try:
        triangle2 = Triangle(7, 3)
        print(triangle2.area)
    except ValueError as e:
        print(e)
    try:
        invalid_triangle = Triangle(-3, 4)
        print(invalid_triangle.area)
    except ValueError as e:
        print(e)