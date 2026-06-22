class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    shape1 = Shape(10.0, 4.0)
    print(shape1.calculate_area())
    
    shape2 = Shape(7.5, 3.2)
    print(shape2.calculate_area())