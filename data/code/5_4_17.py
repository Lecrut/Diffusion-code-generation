# Script to compare two length measurements

def main():
    # Define sample length variables in meters
    length_a = 150.75
    length_b = 82.40
    
    difference = length_a - length_b
    
    if difference > 0:
        print(f"Length A is longer than Length B by {difference:.2f} units.")
    elif difference < 0:
        print(f"Length B is longer than Length A by {-difference:.2f} units.")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()