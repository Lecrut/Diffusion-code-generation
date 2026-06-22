import argparse
import sys

def calculate_weight_difference(weight1, weight2):
    try:
        w1 = float(weight1)
        w2 = float(weight2)
        return abs(w1 - w2)
    except ValueError:
        raise ValueError("Both weights must be numeric values")

def main():
    parser = argparse.ArgumentParser(description='Calculate the difference between two weights.')
    parser.add_argument('weight1', type=str, help='First weight value')
    parser.add_argument('weight2', type=str, help='Second weight value')
    
    args = parser.parse_args()
    
    result = calculate_weight_difference(args.weight1, args.weight2)
    print(result)

if __name__ == '__main__':
    sys.argv = ['script_name', '100', '75']
    main()