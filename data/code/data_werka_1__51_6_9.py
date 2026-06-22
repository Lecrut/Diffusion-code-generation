import argparse

class Shape:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

def main():
    parser = argparse.ArgumentParser(description='Calculate the total perimeter of a shape given its side lengths.')
    parser.add_argument('side_lengths', type=float, nargs='+', help='List of side lengths')
    
    args = parser.parse_args()
    shape = Shape(args.side_lengths)
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == '__main__':
    sample1 = [3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30, 40]
    sample4 = [7]
    
    shape1 = Shape(sample1)
    shape2 = Shape(sample2)
    shape3 = Shape(sample3)
    shape4 = Shape(sample4)
    
    print(f"Perimeter of {sample1}: {shape1.perimeter()}")
    print(f"Perimeter of {sample2}: {shape2.perimeter()}")
    print(f"Perimeter of {sample3}: {shape3.perimeter()}")
    print(f"Perimeter of {sample4}: {shape4.perimeter()}")