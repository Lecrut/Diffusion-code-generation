import argparse

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate difference between two weights.')
    parser.add_argument('--weight1', type=float, help='First weight')
    parser.add_argument('--weight2', type=float, help='Second weight')
    args = parser.parse_args(['--weight1', '10.0', '--weight2', '5.0'])
    difference = calculate_weight_difference(args.weight1, args.weight2)
    print(difference)