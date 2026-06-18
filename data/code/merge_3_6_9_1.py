import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments without making any required, as per constraints on interactive prompts or stdin usage.
    weight1_arg = parser.add_argument('--weight-1', type=float, help='First weight value.')
    weight2_arg = parser.add_argument('--weight-2', type=float, help='Second weight value.')

    # Parse arguments; if not provided via command line and no defaults are set, this will raise an error which is acceptable for a CLI tool.
    args = parser.parse_args()

    # Calculate the difference (Weight 1 - Weight 2)
    result = args.weight_1 - args.weight_2
    
    # Output the calculated difference to standard output
    print(result)

if __name__ == '__main__':
    # Hard-coded sample values provided as command-line arguments for demonstration purposes.
    main()