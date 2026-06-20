import argparse

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight1', type=float, required=True)
    parser.add_argument('--weight2', type=float, required=True)
    args = parser.parse_args(['--weight1', '150.5', '--weight2', '120.0'])
    result = calculate_weight_difference(args.weight1, args.weight2)
    print(result)