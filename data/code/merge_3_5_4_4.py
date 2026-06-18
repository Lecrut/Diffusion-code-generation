# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements in units (e.g., meters)
    length_a = 150.75
    length_b = 98.23
    
    # Calculate the difference between Length A and Length B
    diff = length_a - length_b

    # Conditional statement to print formatted comparison sentence
    if length_a > length_b:
        print(f"Length A is longer than Length B by {diff:.2f} units")
    elif length_b > length_a:
        print(f"Length B is longer than Length A by {abs(diff):.2f} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()