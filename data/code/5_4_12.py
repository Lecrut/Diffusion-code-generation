# Module to compare two length measurements and print a formatted result.
def main():
    # Define sample length values in centimeters (hard-coded)
    length_a = 150
    length_b = 98
    
    # Calculate the difference
    diff = length_a - length_b
    
    # Perform conditional comparison and print formatted sentence based on which is longer
    if length_a > length_b:
        message = f"Length A ({length_a}) is longer than Length B ({length_b}) by {diff} units."
    elif length_b > length_a:
        message = f"Length B ({length_b}) is longer than Length A ({length_a}) by {-1 * diff} units."
    else:
        message = "Length A and Length B are equal in size."
    
    print(message)

if __name__ == '__main__':
    main()