class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def calculate_perimeter(side_a, side_b, side_c):
        return side_a + side_b + side_c

if __name__ == '__main__':
    triangle_sides = [3.0, 4.0, 5.0]
    perimeter = Triangle.calculate_perimeter(*triangle_sides)
    print(perimeter)