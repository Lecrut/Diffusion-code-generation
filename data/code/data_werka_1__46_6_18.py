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
    sample_triangles = [
        (3, 4, 5),
        (5, 12, 13),
        (1, 2, 10),
        (0, 4, 5),
        (3, 3, 3)
    ]

    for sides in sample_triangles:
        a, b, c = sides
        perimeter = TriangleUtils.calculate_perimeter(a, b, c)
        print(f"Perimeter of triangle with sides {a}, {b}, {c}: {perimeter}")