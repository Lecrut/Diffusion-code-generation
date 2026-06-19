class Triangle:
    def __init__(self, a, b, c):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError("Invalid side lengths for a triangle.")
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        triangle = Triangle(side1, side2, side3)
        perimeter = triangle.get_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")