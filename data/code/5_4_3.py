def main():
    # Define two variables for length measurements in meters
    length_a = 150.75
    length_b = 98.32
    
    difference = abs(length_a - length_b)
    
    if length_a > length_b:
        print(f"Length A is longer than Length B by {difference:.2f} units")
    elif length_b > length_a:
        print(f"Length B is longer than Length A by {difference:.2f} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()