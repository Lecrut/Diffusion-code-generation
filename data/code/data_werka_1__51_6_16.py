import argparse

def calculate_perimeter(side_lengths):
    if not side_lengths:
        return 0
    return sum(side_lengths)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon given its side lengths.')
    parser.add_argument('side_lengths', type=float, nargs='+', help='Lengths of the sides of the polygon')
    
    args = parser.parse_args()
    try:
        total_perimeter = calculate_perimeter(args.side_lengths)
        print(total_perimeter)
    except Exception as e:
        print(f"Error: {e}")