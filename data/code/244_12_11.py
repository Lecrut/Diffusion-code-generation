class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive numbers")
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    triangle = Triangle(3, 4)
    trapezoid = Trapezoid(5, 7, 8)
    print(triangle.area())
    print(trapezoid.area())