class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def calculate_area(self):
        import math
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print(f"Triangle 1 Area: {triangle1.calculate_area()}")
    print(f"Triangle 1 Perimeter: {triangle1.calculate_perimeter()}")
    triangle2 = Triangle(6, 8, 10)
    print(f"Triangle 2 Area: {triangle2.calculate_area()}")
    print(f"Triangle 2 Perimeter: {triangle2.calculate_perimeter()}")