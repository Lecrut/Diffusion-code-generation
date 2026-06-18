# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements in meters
    length_a = 150.75
    length_b = 82.3
    
    # Calculate the difference between the two lengths
    diff = abs(length_a - length_b)
    
    # Determine which length is longer and format the output sentence
    if length_a > length_b:
        comparison_text = f"Length A is longer than Length B by {diff:.2f} units."
    elif length_b > length_a:
        comparison_text = f"Length B is longer than Length A by {diff:.2f} units."
    else:
        comparison_text = "Length A and Length B are equal in size."
    
    # Print the formatted result
    print(comparison_text)

if __name__ == '__main__':
    main()