class TriangleUtils:

    @staticmethod
    def validate_sides(a, b, c):
        if not (a > 0 and b > 0 and (c > 0)):
            raise ValueError('Sides must be positive numbers')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Triangle inequality not satisfied')

    @staticmethod
    def calculate_perimeter(a, b, c):
        TriangleUtils.validate_sides(a, b, c)
        return a + b + c
if __name__ == '__main__':
    try:
        perimeter1 = TriangleUtils.calculate_perimeter(3, 4, 5)
        print(perimeter1)
        perimeter2 = TriangleUtils.calculate_perimeter(5, 12, 13)
        print(perimeter2)
        invalid_perimeter = TriangleUtils.calculate_perimeter(1, 2, 10)
    except ValueError as e:
        print(e)