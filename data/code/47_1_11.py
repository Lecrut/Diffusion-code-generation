class Triangle:
    def __init__(self, base, height):
        try:
            self.base = float(base)
            self.height = float(height)
            if self.base < 0 or self.height < 0:
                raise ValueError("Base and height must be non-negative.")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid input: Both base and height must be valid numbers. Error: {e}")

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle1 = Triangle(4.0, 5.0)
        print(triangle1.area())
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        triangle2 = Triangle(10.5, 2.0)
        print(triangle2.area())
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        triangle3 = Triangle(-3.0, 4.0)
        print(triangle3.area())
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        triangle4 = Triangle("a", 5.0)
        print(triangle4.area())
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        triangle5 = Triangle(7.0, -2.0)
        print(triangle5.area())
    except ValueError as e:
        print(f"Error caught: {e}")