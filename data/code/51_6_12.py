import argparse

def calculate_perimeter(side_lengths):
    if not all((isinstance(length, (int, float)) and length > 0 for length in side_lengths)):
        raise ValueError('All side lengths must be positive numbers.')
    return sum(side_lengths)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon given its side lengths.')
    parser.add_argument('side_lengths', type=float, nargs='+', help='The lengths of the sides of the polygon.')
    try:
        args = parser.parse_args()
        perimeter = calculate_perimeter(args.side_lengths)
        print(perimeter)
        sample1 = [3, 4, 5]
        sample2 = [10, 20, 30, 40]
        sample3 = [7]
        print(calculate_perimeter(sample1))
        print(calculate_perimeter(sample2))
        print(calculate_perimeter(sample3))
    except ValueError as e:
        print(e)