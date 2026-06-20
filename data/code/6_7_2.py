import argparse

def calculate_weight_difference(weight_one, weight_two):
    return abs(weight_one - weight_two)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('weight_one', type=float, help='First weight')
    parser.add_argument('weight_two', type=float, help='Second weight')
    args = parser.parse_args()
    result = calculate_weight_difference(args.weight_one, args.weight_two)
    print(result)