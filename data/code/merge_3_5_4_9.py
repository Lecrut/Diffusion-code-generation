import sys

def main():
    """Defines two length variables and prints a formatted comparison."""
    
    # Define sample lengths in meters
    length_a = 50.75
    length_b = 32.4
    
    # Calculate the difference
    diff = abs(length_a - length_b)
    
    # Determine which is longer and format the output sentence
    if length_a > length_b:
        comparison_sentence = f"Length A ({length_a}m) is longer than Length B ({length_b}m) by {diff:.2f} units."
    elif length_b > length_a:
        comparison_sentence = f"Length B ({length_b}m) is longer than Length A ({length_a}m) by {diff:.2f} units."
    else:
        comparison_sentence = "Length A and Length B are equal, differing by 0.00 units."
    
    print(comparison_sentence)

if __name__ == '__main__':
    main()