import argparse

def calculate_perimeter(side_lengths):
    return sum(side_lengths)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon given side lengths.')
    parser.add_argument('sides', type=float, nargs='+', help='Lengths of the sides of the polygon')
    args = parser.parse_args()
    
    sample1 = [3.0, 4.0, 5.0]
    sample2 = []
    sample3 = [10.0, 20.0, 30.0, 40.0]
    sample4 = [7.0]

    print(f"Perimeter of {sample1}: {calculate_perimeter(sample1)}")
    print(f"Perimeter of {sample2}: {calculate_perimeter(sample2)}")
    print(f"Perimeter of {sample3}: {calculate_perimeter(sample3)}")
    print(f"Perimeter of {sample4}: {calculate_perimeter(sample4)}")