import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments with defaults to avoid requiring input on command line or interactive prompts
    weight1 = parser.add_argument('--weight1', type=float, default=50.0)
    weight2 = parser.add_argument('--weight2', type=float, default=30.0)

    args = parser.parse_args()

    difference = args.weight1 - args.weight2
    
    print(f"{difference:.4f}")

if __name__ == '__main__':
    main()