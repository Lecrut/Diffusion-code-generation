import argparse

def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('weight1', type=float, default=150.0)
    parser.add_argument('weight2', type=float, default=120.0)
    args = parser.parse_args()
    result = calculate_difference(args.weight1, args.weight2)
    print(result)