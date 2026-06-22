import math

class Triangle:
    MIN_VALID_LENGTH = 0.1
    
    @staticmethod
    def is_valid_triangle(a, b, c):
        return (a > Triangle.MIN_VALID_LENGTH and 
                b > Triangle.MIN_VALID_LENGTH and 
                c > Triangle.MIN_VALID_LENGTH and
                a + b > c and
                a + c > b and
                b + c > a)
    
    @staticmethod
    def calculate_area(sides):
        if len(sides) != 3:
            raise ValueError('Exactly three sides are required for a triangle.')
        a, b, c = sides
        if not Triangle.is_valid_triangle(a, b, c):
            raise ValueError('The given sides do not form a valid triangle.')
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        area = Triangle.calculate_area(sides)
        print(area)
    except ValueError as e:
        print(e)