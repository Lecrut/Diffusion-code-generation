import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define non-required arguments as per constraints (no input(), sys.stdin, etc.)
    weight1_arg = parser.add_argument(
        "weight1", 
        type=float, 
        help="The first weight value."
    )
    
    weight2_arg = parser.add_argument(
        "weight2", 
        type=float, 
        help="The second weight value."
    )
    
    args = parser.parse_args()

    # Calculate and print the difference to standard output
    difference = weight1_arg - weight2_arg
    print(f"{difference:.6f}")

if __name__ == '__main__':
    main()