import argparse

class ShapeCalculator:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        if not self.side_lengths:
            return 0
        return sum(self.side_lengths)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a shape given its side lengths.')
    parser.add_argument('side_lengths', type=int, nargs='+', help='List of side lengths')

    args = parser.parse_args()
    calculator = ShapeCalculator(args.side_lengths)
    
    sample1 = [3, 4, 5]
    sample2 = [10, 20, 30, 40]
    sample3 = []
    sample4 = [7]

    print(f"Perimeter of {sample1}: {ShapeCalculator(sample1).calculate_perimeter()}")
    print(f"Perimeter of {sample2}: {ShapeCalculator(sample2).calculate_perimeter()}")
    print(f"Perimeter of {sample3}: {ShapeCalculator(sample3).calculate_perimeter()}")
    print(f"Perimeter of {sample4}: {ShapeCalculator(sample4).calculate_perimeter()}")