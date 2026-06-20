import argparse

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description='Calculate the difference between two weights.')
    parser.add_argument('--weight1', type=float, required=True, help='First weight value')
    parser.add_argument('--weight2', type=float, required=True, help='Second weight value')
    arguments = parser.parse_args(args)
    return arguments.weight1, arguments.weight2

if __name__ == '__main__':
    w1, w2 = parse_arguments(['--weight1', '10.5', '--weight2', '7.2'])
    result = calculate_weight_difference(w1, w2)
    print(result)