import argparse

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight1', type=float, default=10.0)
    parser.add_argument('--weight2', type=float, default=5.0)
    args = parser.parse_args()
    difference = calculate_weight_difference(args.weight1, args.weight2)
    print(difference)

if __name__ == '__main__':
    main()