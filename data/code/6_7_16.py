import argparse

def calculate_weight_difference(weight_a, weight_b):
    return weight_a - weight_b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two weights.')
    parser.add_argument('weight_a', type=float, help='The first weight.')
    parser.add_argument('weight_b', type=float, help='The second weight.')

    args = parser.parse_args(['10.5', '3.2'])

    result = calculate_weight_difference(args.weight_a, args.weight_b)
    print(result)