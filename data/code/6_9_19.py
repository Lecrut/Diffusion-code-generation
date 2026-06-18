import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define weight arguments with defaults to avoid requiring input from user or files
    w1_parser = parser.add_argument('--w1', type=float, default=50.0)
    w2_parser = parser.add_argument('--w2', type=float, default=30.0)
    
    args = parser.parse_args()
    
    difference = args.w1 - args.w2
    
    print(f"{difference:.6f}")

if __name__ == '__main__':
    main()