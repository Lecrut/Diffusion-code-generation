import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments with defaults to avoid requiring input from user or command line
    weight1_arg = parser.add_argument(
        '--weight1', 
        type=float, 
        default=5.0, 
        help='First weight value (default: 5.0)'
    )
    weight2_arg = parser.add_argument(
        '--weight2', 
        type=float, 
        default=3.0, 
        help='Second weight value (default: 3.0)'
    )

    args = parser.parse_args()

    # Calculate the difference
    difference = weight1_arg - weight2_arg
    
    # Output result to standard output
    print(f"{difference:.4f}")

if __name__ == '__main__':
    main()