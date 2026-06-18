# Script to compare two length measurements using conditional statements

def main():
    # Define sample lengths in meters
    length_a = 150.75
    length_b = 98.23
    
    difference = length_a - length_b
    
    if length_a > length_b:
        print(f"Length A is longer than Length B by {difference:.2f} units")
    elif length_b > length_a:
        diff_val = length_b - length_a
        print(f"Length B is longer than Length A by {diff_val:.2f} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()