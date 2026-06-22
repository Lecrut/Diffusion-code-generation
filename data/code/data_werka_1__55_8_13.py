class Triangle:

    def __init__(self, side1, side2, side3):
        if not (side1 + side2 > side3 and side1 + side3 > side2 and (side2 + side3 > side1)):
            raise ValueError('Invalid triangle side lengths')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 10
        side_c = 5
        triangle = Triangle(side_a, side_b, side_c)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)