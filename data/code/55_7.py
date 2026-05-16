class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    perimeter = t.calculate_perimeter()
    print(perimeter)