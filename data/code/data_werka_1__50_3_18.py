import argparse

def calculate_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    result = calculate_difference(args.area1, args.area2)
    print(f'Command-line difference: {result}')
    SAMPLE_AREA1 = 60.0
    SAMPLE_AREA2 = 40.0
    sample_result = calculate_difference(SAMPLE_AREA1, SAMPLE_AREA2)
    print(f'Sample difference: {sample_result}')