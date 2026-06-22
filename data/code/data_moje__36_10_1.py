class Trapezoid:
    def __init__(self, base1, base2, height):
        if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height values must be numeric")
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Base and height values must be positive")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height * 0.5

if __name__ == '__main__':
    t1 = Trapezoid(10.0, 15.0, 6.0)
    t2 = Trapezoid(5, 8, 4)
    print(t1.area())
    print(t2.area())