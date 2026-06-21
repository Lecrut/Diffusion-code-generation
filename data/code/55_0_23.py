class Triangle:
    def __init__(self, side1, side2, side3):
        if not (side1 > 0 and side2 > 0 and side3 > 0):
            raise ValueError("All sides must be positive")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)