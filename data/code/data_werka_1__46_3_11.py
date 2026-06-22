import argparse

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not (side1 > 0 and side2 > 0 and (side3 > 0)):
            raise ValueError('Side lengths must be positive.')
        if not (side1 + side2 > side3 and side1 + side3 > side2 and (side2 + side3 > side1)):
            raise ValueError('The given side lengths do not form a valid triangle.')

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

def main():
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle.')
    parser.add_argument('side1', type=float, help='Length of the first side')
    parser.add_argument('side2', type=float, help='Length of the second side')
    parser.add_argument('side3', type=float, help='Length of the third side')
    args = parser.parse_args()
    try:
        triangle = Triangle(args.side1, args.side2, args.side3)
        print(f'Perimeter: {triangle.perimeter()}')
    except ValueError as e:
        print(f'Error: {e}')
if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f'Perimeter of (3, 4, 5): {triangle1.perimeter()}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        triangle2 = Triangle(7, 8, 9)
        print(f'Perimeter of (7, 8, 9): {triangle2.perimeter()}')
    except ValueError as e:
        print(f'Error: {e}')