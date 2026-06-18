import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments with defaults to avoid requiring user input
    weight1_arg = parser.add_argument(
        '--weight-1', type=float, default=50.0, help='First weight value (default: 50.0)'
    )
    weight2_arg = parser.add_argument(
        '--weight-2', type=float, default=30.0, help='Second weight value (default: 30.0)'
    )

    args = parser.parse_args()

    # Calculate the difference
    difference = weight1_arg - weight2_arg
    
    # Output to standard output
    print(f"{difference}")

if __name__ == '__main__':
    main()