import argparse

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    parser.add_argument("--weight1", type=float, default=75.5, help="First weight")
    parser.add_argument("--weight2", type=float, default=80.2, help="Second weight")
    args = parser.parse_args()
    difference = calculate_weight_difference(args.weight1, args.weight2)
    print(difference)

if __name__ == '__main__':
    main()