import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define non-required arguments with defaults to avoid interactive prompts or errors on missing input
    weight1_arg = parser.add_argument('--weight-1', type=float, default=0.5)
    weight2_arg = parser.add_argument('--weight-2', type=float, default=1.0)
    
    args = parser.parse_args()
    
    difference = abs(args.weight1 - args.weight2)
    print(f"{difference:.4f}")

if __name__ == '__main__':
    main()