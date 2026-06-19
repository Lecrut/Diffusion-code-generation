class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def is_valid_triangle(self):
        a, b, c = sorted(self.sides)
        return a + b > c

    def get_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        perimeter = triangle.get_perimeter()
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")