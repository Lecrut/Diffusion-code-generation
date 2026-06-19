import argparse

class AreaCalculator:
    @staticmethod
    def calculate_difference(area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    result = AreaCalculator.calculate_difference(args.area1, args.area2)
    print(result)
    sample_area1 = 60.0
    sample_area2 = 35.0
    sample_result = AreaCalculator.calculate_difference(sample_area1, sample_area2)
    print(f'Sample difference: {sample_result}')