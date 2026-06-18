import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define weight arguments with defaults to avoid requiring input
    w1_parser = parser.add_argument_group('Weight 1')
    w1_parser.add_argument('--w1', type=float, default=5.0)
    
    w2_parser = parser.add_argument_group('Weight 2')
    w2_parser.add_argument('--w2', type=float, default=3.0)

    args = parser.parse_args()
    
    difference = args.w1 - args.w2
    
    print(f"Difference: {difference}")

if __name__ == '__main__':
    main()