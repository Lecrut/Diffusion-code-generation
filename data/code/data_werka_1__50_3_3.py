import argparse

def calculate_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    
    calculated_difference = calculate_difference(args.area1, args.area2)
    print(calculated_difference)
    
    sample_area1 = 75.0
    sample_area2 = 25.0
    sample_diff = calculate_difference(sample_area1, sample_area2)
    print(f'Sample difference: {sample_diff}')