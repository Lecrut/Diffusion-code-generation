class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        try:
            base = float(self.base)
            height = float(self.height)
            if base < 0 or height < 0:
                raise ValueError("Base and height must be non-negative.")
            return 0.5 * base * height
        except (TypeError, ValueError) as e:
            return f"Error: {e}"

if __name__ == '__main__':
    triangle1 = Triangle(4.0, 5.0)
    print(triangle1.area())

    triangle2 = Triangle(10.5, 2.0)
    print(triangle2.area())

    triangle3 = Triangle(-3.0, 4.0)
    print(triangle3.area())

    triangle4 = Triangle("a", 5.0)
    print(triangle4.area())

    triangle5 = Triangle(7.0, -2.0)
    print(triangle5.area())