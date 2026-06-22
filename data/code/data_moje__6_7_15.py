import argparse

def calculate_difference(weight_a, weight_b):
    return weight_a - weight_b

if __name__ == '__main__':
    sample_weight_a = 150.0
    sample_weight_b = 120.5
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight-a', type=float, required=False, default=sample_weight_a)
    parser.add_argument('--weight-b', type=float, required=False, default=sample_weight_b)
    args = parser.parse_args()
    result = calculate_difference(args.weight_a, args.weight_b)
    print(result)