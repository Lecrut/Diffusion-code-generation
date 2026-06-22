class Trapezoid:
    def __init__(self, base1, base2, height):
        if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("All dimensions must be numbers.")
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    t = Trapezoid(5, 7, 4)
    print(t.area())