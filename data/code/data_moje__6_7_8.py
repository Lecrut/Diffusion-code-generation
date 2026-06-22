import argparse

def calculate_weight_difference(w1, w2):
    return abs(w1 - w2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the absolute difference between two weights.')
    parser.add_argument('weight1', type=float, help='First weight value')
    parser.add_argument('weight2', type=float, help='Second weight value')
    args = parser.parse_args()

    result = calculate_weight_difference(args.weight1, args.weight2)
    print(result)