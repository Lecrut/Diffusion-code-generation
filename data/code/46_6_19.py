class TriangleUtils:
    @staticmethod
    def is_valid_triangle(a, b, c):
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    @staticmethod
    def calculate_perimeter(a, b, c):
        if not TriangleUtils.is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides")
        return a + b + c

if __name__ == '__main__':
    try:
        perimeter1 = TriangleUtils.calculate_perimeter(3, 4, 5)
        print(f"Perimeter of triangle with sides 3, 4, 5: {perimeter1}")
        
        perimeter2 = TriangleUtils.calculate_perimeter(7, 8, 9)
        print(f"Perimeter of triangle with sides 7, 8, 9: {perimeter2}")
        
        invalid_perimeter = TriangleUtils.calculate_perimeter(1, 2, 10)
    except ValueError as e:
        print(e)