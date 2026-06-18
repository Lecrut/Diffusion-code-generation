# Script to compare two length measurements using conditional statements

def main():
    # Define sample values for Length A and Length B in meters
    len_a = 50.75
    len_b = 42.30
    
    # Calculate the difference between the two lengths
    diff = len_a - len_b
    
    print(f"Length A is longer than Length B by {diff:.2f} units")

if __name__ == '__main__':
    main()