import argparse

def calculate_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a polygon.')
    parser.add_argument('sides', type=float, nargs='+', help='Lengths of the sides of the polygon')
    
    args = parser.parse_args()
    perimeter = calculate_perimeter(args.sides)
    print(perimeter)