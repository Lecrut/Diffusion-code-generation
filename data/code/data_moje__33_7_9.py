from decimal import Decimal, getcontext
getcontext().prec = 10

class Triangle:
    def __init__(self, base_val, height_val):
        if base_val <= 0 or height_val <= 0:
            raise ValueError("Dimensions must be positive")
        self.base = Decimal(str(base_val))
        self.height = Decimal(str(height_val))

    def get_area(self):
        return self.base * self.height * Decimal("0.5")

    def get_perimeter_base_height(self):
        return self.base + self.height

if __name__ == '__main__':
    b = 12.345
    h = 6.789
    tri = Triangle(b, h)
    print(tri.get_area())
    print(tri.get_perimeter_base_height())