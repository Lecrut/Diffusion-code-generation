# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements in meters
    length_a = 150.75
    
    length_b = 82.30
    
    difference = length_a - length_b
    
    if length_a > length_b:
        comparison_message = f'Length A is longer than Length B by {difference:.2f} units.'
    elif length_b > length_a:
        comparison_message = f'Length B is longer than Length A by {abs(difference):.2f} units.'
    else:
        comparison_message = 'Length A and Length B are equal.'
    
    print(comparison_message)

if __name__ == '__main__':
    main()