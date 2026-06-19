import argparse

def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon given its side lengths.')
    parser.add_argument('sides', type=float, nargs='+', help='Lengths of the sides of the polygon')
    args = parser.parse_args()
    sample1 = [5.5, 6.5, 7.5]
    sample2 = [8.0, 9.0, 10.0, 11.0]
    sample3 = []
    sample4 = [12.3]
    perimeter1 = calculate_perimeter(sample1)
    perimeter2 = calculate_perimeter(sample2)
    perimeter3 = calculate_perimeter(sample3)
    perimeter4 = calculate_perimeter(sample4)
    print(f'Perimeter of {sample1}: {perimeter1}')
    print(f'Perimeter of {sample2}: {perimeter2}')
    print(f'Perimeter of {sample3}: {perimeter3}')
    print(f'Perimeter of {sample4}: {perimeter4}')