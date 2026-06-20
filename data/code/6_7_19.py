import argparse

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

def setup_parser():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    parser.add_argument("weight1", type=float, help="First weight value.")
    parser.add_argument("weight2", type=float, help="Second weight value.")
    return parser

if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args(['10.5', '5.0'])
    result = calculate_weight_difference(args.weight1, args.weight2)
    print(result)