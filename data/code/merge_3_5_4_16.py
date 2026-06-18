# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements in meters
    len_a = 50.75
    len_b = 32.4
    
    # Calculate the difference between the two lengths
    diff = len_a - len_b
    
    print(f"Length A is longer than Length B by {diff} units")

if __name__ == '__main__':
    main()