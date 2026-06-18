# Script to compare two length measurements using conditional statements

def main():
    # Define sample lengths in meters
    len_a = 10.5
    len_b = 7.2
    
    difference = abs(len_a - len_b)
    
    if len_a > len_b:
        print(f"Length A is longer than Length B by {difference:.1f} units")
    elif len_b > len_a:
        print(f"Length B is longer than Length A by {difference:.1f} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()