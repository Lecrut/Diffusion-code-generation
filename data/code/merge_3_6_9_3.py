import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments without making them required to avoid interactive prompts or errors on missing args in sample block logic if desired, 
    # but per task "Never call input(), sys.stdin, argparse required arguments", we will define them as optional for safety in non-interactive contexts.
    parser.add_argument("--weight1", type=float, default=0.0, help="First weight value.")
    parser.add_argument("--weight2", type=float, default=0.0, help="Second weight value.")

    # Parse arguments (will use defaults if none provided)
    args = parser.parse_args()

    # Calculate the difference
    difference = args.weight1 - args.weight2
    
    # Output result to standard output
    print(f"{difference}")

if __name__ == '__main__':
    main()