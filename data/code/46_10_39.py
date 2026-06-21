class Triangle:
    MIN_SIDE_LENGTH = 0.0

    @staticmethod
    def is_valid_triangle(a, b, c):
        return (a > Triangle.MIN_SIDE_LENGTH and b > Triangle.MIN_SIDE_LENGTH and c > Triangle.MIN_SIDE_LENGTH) and \
               ((a + b > c) and (a + c > b) and (b + c > a))

    @staticmethod
    def calculate_perimeter(a, b, c):
        if not Triangle.is_valid_triangle(a, b, c):
            raise ValueError('The given sides do not form a valid triangle')
        return a + b + c

if __name__ == '__main__':
    side1 = 5.0
    side2 = 12.0
    side3 = 13.0
    try:
        perimeter = Triangle.calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)