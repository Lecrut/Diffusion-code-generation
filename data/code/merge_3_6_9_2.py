import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Create non-required arguments to satisfy constraints without user input interaction
    weight1_arg = parser.add_argument("--weight1", type=float, help="First weight value")
    weight2_arg = parser.add_argument("--weight2", type=float, help="Second weight value")

    args = parser.parse_args()

    # Use hard-coded sample values if no arguments are provided
    sample_weight1 = 50.0
    sample_weight2 = 30.0
    
    if args.weight1 is None:
        w1 = sample_weight1
    else:
        w1 = args.weight1
        
    if args.weight2 is None:
        w2 = sample_weight2
    else:
        w2 = args.weight2

    difference = w1 - w2
    
    print(difference)

if __name__ == '__main__':
    main()