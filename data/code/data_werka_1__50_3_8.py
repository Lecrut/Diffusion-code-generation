import argparse

def calculate_difference(area1, area2):
    try:
        result = abs(float(area1) - float(area2))
        return result
    except ValueError as e:
        raise ValueError("Both inputs must be valid numbers.") from e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two areas.')
    parser.add_argument('area1', help='The first area value')
    parser.add_argument('area2', help='The second area value')
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