class Triangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle1 = Triangle(4.0, 5.0)
        print(triangle1.calculate_area())
    except ValueError as e:
        print(e)

    try:
        triangle2 = Triangle(10.5, 2.0)
        print(triangle2.calculate_area())
    except ValueError as e:
        print(e)

    try:
        triangle3 = Triangle(-3.0, 4.0)
        print(triangle3.calculate_area())
    except ValueError as e:
        print(e)

    try:
        triangle4 = Triangle("a", 5.0)
        print(triangle4.calculate_area())
    except ValueError as e:
        print(e)

    try:
        triangle5 = Triangle(7.0, -2.0)
        print(triangle5.calculate_area())
    except ValueError as e:
        print(e)