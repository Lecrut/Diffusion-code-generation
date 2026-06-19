class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calculate_perimeter(self):
        if not Triangle.is_valid_triangle(self.side_a, self.side_b, self.side_c):
            raise ValueError("Invalid triangle sides")
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    try:
        t = Triangle(3.0, 4.0, 5.0)
        perimeter = t.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)