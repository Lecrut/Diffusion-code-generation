import argparse

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    parser.add_argument("weight1", type=float, help="First weight")
    parser.add_argument("weight2", type=float, help="Second weight")
    
    args = parser.parse_args()
    
    result = calculate_weight_difference(args.weight1, args.weight2)
    print(result)

if __name__ == '__main__':
    main()