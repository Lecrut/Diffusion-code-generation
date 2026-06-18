import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
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

    difference = weight1_arg - weight2_arg
    
    # Output the result to standard output without printing extra labels since argparse handles description and error messages.
    print(difference)

if __name__ == '__main__':
    main()