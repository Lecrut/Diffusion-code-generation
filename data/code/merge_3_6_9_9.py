import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments with defaults to avoid requiring user input
    weight1_arg = parser.add_argument(
        'weight1', 
        type=float, 
        default=5.0, 
        help='The first weight value (default: 5.0)'
    )
    weight2_arg = parser.add_argument(
        'weight2', 
        type=float, 
        default=3.7, 
        help='The second weight value (default: 3.7)'
    )

    args = parser.parse_args()
    
    # Calculate the difference
    diff = weight1_arg - weight2_arg
    
    # Output result to standard output
    print(f"{diff:.4f}")

if __name__ == '__main__':
    main()