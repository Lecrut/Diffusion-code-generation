class TriangleUtils:

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a > 0 and b > 0 and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

    @staticmethod
    def calculate_perimeter(a, b, c):
        if TriangleUtils.is_valid_triangle(a, b, c):
            return a + b + c
        else:
            return None
if __name__ == '__main__':
    print(TriangleUtils.calculate_perimeter(3, 4, 5))
    print(TriangleUtils.calculate_perimeter(10, 6, 8))
    print(TriangleUtils.calculate_perimeter(1, 2, 10))
    print(TriangleUtils.calculate_perimeter(0, 5, 5))