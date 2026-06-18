import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define arguments with defaults to avoid requiring input from user or command line flags in a strict sense, 
    # though typically these are passed via CLI args. The task says "accepts two weight arguments", implying they should be provided.
    # However, it also forbids argparse required arguments and interactive prompts. To satisfy both: we use optional arguments with defaults for the sample run, 
    # but allow them to be overridden if needed in a real usage scenario (though not enforced here).
    
    weight1 = parser.add_argument('--weight1', type=float, default=50.0)
    weight2 = parser.add_argument('--weight2', type=float, default=30.0)

    args = parser.parse_args()

    difference = args.weight1 - args.weight2
    
    print(difference)

if __name__ == '__main__':
    main()