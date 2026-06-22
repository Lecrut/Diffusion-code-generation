class ShapeCalculator:
    def kite_area(self, d1, d2):
        return 0.5 * d1 * d2
    
    def circle_area(self, radius):
        import math
        return math.pi * (radius ** 2)
    
    def total_area(self, kite_d1, kite_d2, circle_radius):
        return self.kite_area(kite_d1, kite_d2) + self.circle_area(circle_radius)

if __name__ == '__main__':
    calculator = ShapeCalculator()
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    total_area = calculator.total_area(kite_d1, kite_d2, circle_radius)
    print(total_area)