class Triangle:
    def __init__(self, side1, side2, side3):
        if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and isinstance(side3, (int, float))):
            raise ValueError("All sides must be numbers.")
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive numbers.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given sides do not form a valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_perimeter())
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")