# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements (in meters)
    length_a = 150
    length_b = 87
    
    # Calculate the difference between the lengths
    diff = length_a - length_b
    
    # Conditional statement to print a formatted comparison sentence
    if length_a > length_b:
        print(f"Length A is longer than Length B by {diff} units")
    elif length_b > length_a:
        print(f"Length B is longer than Length A by {-diff} units")
    else:
        print("Both lengths are equal.")

if __name__ == '__main__':
    main()