import argparse

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference between two weights.')
    parser.add_argument('weight1', type=float, help='The first weight')
    parser.add_argument('weight2', type=float, help='The second weight')
    args = parser.parse_args()
    difference = calculate_weight_difference(args.weight1, args.weight2)
    print(difference)
sample_weight1 = 75.0
sample_weight2 = 68.0
print(calculate_weight_difference(sample_weight1, sample_weight2))