import argparse

def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon given its side lengths.')
    parser.add_argument('sides', type=float, nargs='+', help='List of side lengths')
    args = parser.parse_args()
    sample1 = [3, 4, 5]
    sample2 = [10, 20, 30, 40]
    sample3 = [7]
    print(f'Perimeter of {sample1}: {calculate_perimeter(sample1)}')
    print(f'Perimeter of {sample2}: {calculate_perimeter(sample2)}')
    print(f'Perimeter of {sample3}: {calculate_perimeter(sample3)}')