import argparse

class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    
    calculator = AreaDifferenceCalculator(args.area1, args.area2)
    print(calculator.calculate_difference())
    
    sample_calculator = AreaDifferenceCalculator(50.0, 30.0)
    print(sample_calculator.calculate_difference())