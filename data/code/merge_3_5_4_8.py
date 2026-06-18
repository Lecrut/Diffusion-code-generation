# Script to compare two length measurements

def main():
    # Define sample lengths in meters
    length_a = 150.5
    length_b = 42.8
    
    difference = length_a - length_b
    
    if difference > 0:
        print(f"Length A is longer than Length B by {difference:.2f} units")
    elif difference < 0:
        print(f"Length B is longer than Length A by {-difference:.2f} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()