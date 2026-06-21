class Triangle:
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
        if self.base < 0 or self.height < 0:
            raise ValueError("Base and height must be non-negative.")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle1 = Triangle(10, 5)
        print(f"Area of triangle1: {triangle1.calculate_area()}")
        
        triangle2 = Triangle(7.5, 3.2)
        print(f"Area of triangle2: {triangle2.calculate_area()}")
        
        triangle3 = Triangle(-3, 4)
        print(f"Area of triangle3: {triangle3.calculate_area()}")
    except ValueError as e:
        print(e)