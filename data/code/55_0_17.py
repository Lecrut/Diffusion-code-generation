class Triangle:

    def __init__(self, side1, side2, side3):
        if not (side1 > 0 and side2 > 0 and (side3 > 0)):
            raise ValueError('All sides must be positive numbers.')
        if not (side1 + side2 > side3 and side1 + side3 > side2 and (side2 + side3 > side1)):
            raise ValueError('The given side lengths do not form a valid triangle.')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(triangle1.get_perimeter())
        triangle2 = Triangle(6, 8, 10)
        print(triangle2.get_perimeter())
        invalid_triangle = Triangle(1, 1, 2)
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')