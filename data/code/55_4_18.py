class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid(self):
        return (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1)

    def calculate_perimeter(self):
        if not self.is_valid():
            raise ValueError("The given side lengths do not form a valid triangle.")
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        perimeter1 = triangle1.calculate_perimeter()
        print(f"Perimeter of (3, 4, 5): {perimeter1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(7, 10, 5)
        perimeter2 = triangle2.calculate_perimeter()
        print(f"Perimeter of (7, 10, 5): {perimeter2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle3 = Triangle(1, 2, 10)
        perimeter3 = triangle3.calculate_perimeter()
        print(f"Perimeter of (1, 2, 10): {perimeter3}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle4 = Triangle(5, 5, 5)
        perimeter4 = triangle4.calculate_perimeter()
        print(f"Perimeter of (5, 5, 5): {perimeter4}")
    except ValueError as e:
        print(f"Error: {e}")