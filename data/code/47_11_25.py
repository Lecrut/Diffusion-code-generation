import math

class Triangle:
    EPSILON = 1e-10

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    @staticmethod
    def calculate_area(a, b, c):
        if not Triangle.is_valid_triangle(a, b, c):
            raise ValueError('The given side lengths do not form a valid triangle')
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 10
        side_c = 5
        area = Triangle.calculate_area(side_a, side_b, side_c)
        print(f'The area of the triangle with sides {side_a}, {side_b}, and {side_c} is: {area}')
    except ValueError as e:
        print(e)