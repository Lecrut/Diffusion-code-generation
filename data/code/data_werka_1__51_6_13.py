import argparse

class Shape:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    sample1 = [3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30, 40]
    sample4 = [7]

    shape1 = Shape(sample1)
    shape2 = Shape(sample2)
    shape3 = Shape(sample3)
    shape4 = Shape(sample4)

    print(f"Perimeter of {sample1}: {shape1.calculate_perimeter()}")
    print(f"Perimeter of {sample2}: {shape2.calculate_perimeter()}")
    print(f"Perimeter of {sample3}: {shape3.calculate_perimeter()}")
    print(f"Perimeter of {sample4}: {shape4.calculate_perimeter()}")