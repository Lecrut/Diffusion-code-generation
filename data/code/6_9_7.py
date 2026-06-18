import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments but do not make any required to avoid blocking on missing input in non-interactive contexts if needed, 
    # though per task constraints we will ensure sample block provides values.
    weight1 = parser.add_argument('--weight1', type=float)
    weight2 = parser.add_argument('--weight2', type=float)

    args = parser.parse_args()

    # Ensure arguments are provided for calculation safety in this context
    if args.weight1 is None or args.weight2 is None:
        raise ValueError("Both --weight1 and --weight2 must be provided.")

    difference = args.weight1 - args.weight2
    
    print(difference)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    
    main()