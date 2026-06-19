class TriangleUtils:
    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

    @staticmethod
    def calculate_perimeter(a, b, c):
        if TriangleUtils.is_valid_triangle(a, b, c):
            return a + b + c
        else:
            return None

if __name__ == '__main__':
    sample_values = {
        'triangle1': (3, 4, 5),
        'triangle2': (5, 12, 13),
        'invalid_triangle1': (1, 2, 10),
        'invalid_triangle2': (0, 4, 5)
    }

    for name, sides in sample_values.items():
        perimeter = TriangleUtils.calculate_perimeter(*sides)
        print(f"Perimeter of {name}: {perimeter}")