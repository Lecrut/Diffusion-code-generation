import argparse

class AreaCalculator:

    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    @staticmethod
    def calculate_difference(area1, area2):
        return abs(area1 - area2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    calculator = AreaCalculator(args.area1, args.area2)
    difference = calculator.calculate_difference(calculator.area1, calculator.area2)
    print(difference)
    sample_area1 = 60.0
    sample_area2 = 35.0
    sample_calculator = AreaCalculator(sample_area1, sample_area2)
    sample_difference = sample_calculator.calculate_difference(sample_calculator.area1, sample_calculator.area2)
    print(sample_difference)