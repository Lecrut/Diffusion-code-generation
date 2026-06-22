class Triangle:

    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
        if self.base < 0 or self.height < 0:
            raise ValueError('Base and height must be non-negative.')

    def area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    try:
        triangle1 = Triangle(6.0, 8.0)
        print(f'Area of triangle1: {triangle1.area()}')
        triangle2 = Triangle(3.5, 4.2)
        print(f'Area of triangle2: {triangle2.area()}')
        triangle3 = Triangle(-2.0, 3.0)
        print(triangle3.area())
    except ValueError as e:
        print(f'Error caught: {e}')