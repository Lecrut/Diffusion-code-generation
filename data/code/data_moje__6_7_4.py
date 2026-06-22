import argparse

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight1', type=float)
    parser.add_argument('--weight2', type=float)
    args = parser.parse_args()

    if args.weight1 is not None and args.weight2 is not None:
        result = calculate_weight_difference(args.weight1, args.weight2)
        print(result)

if __name__ == '__main__':
    sample_weight1 = 75.5
    sample_weight2 = 68.2
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)