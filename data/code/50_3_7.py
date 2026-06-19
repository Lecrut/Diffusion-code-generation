import argparse

def calculate_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    result = calculate_difference(args.area1, args.area2)
    print(result)
    sample_areas = {'sample1': {'area1': 60.0, 'area2': 35.0}, 'sample2': {'area1': 80.0, 'area2': 40.0}}
    for key, areas in sample_areas.items():
        sample_result = calculate_difference(areas['area1'], areas['area2'])
        print(f'{key} difference: {sample_result}')