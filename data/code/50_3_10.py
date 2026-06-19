import argparse

def validate_area(area):
    if area < 0:
        raise ValueError('Area value cannot be negative')
    return area

def calculate_difference(area1, area2):
    validated_area1 = validate_area(area1)
    validated_area2 = validate_area(area2)
    return abs(validated_area1 - validated_area2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', type=float, help='The first area value')
    parser.add_argument('area2', type=float, help='The second area value')
    args = parser.parse_args()
    try:
        result = calculate_difference(args.area1, args.area2)
        print(result)
    except ValueError as e:
        print(e)
    sample_area1 = 60.0
    sample_area2 = 20.0
    try:
        sample_result = calculate_difference(sample_area1, sample_area2)
        print(f'Sample difference: {sample_result}')
    except ValueError as e:
        print(e)