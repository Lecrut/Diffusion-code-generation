import argparse

def compute_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    first_area = args.area1
    second_area = args.area2
    difference = compute_difference(first_area, second_area)
    print(difference)
    sample_first_area = 80.5
    sample_second_area = 45.3
    sample_diff = compute_difference(sample_first_area, sample_second_area)
    print(f'Sample difference: {sample_diff}')