import sys

def check_negative(value):
    """Checks if a given integer is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    test_values = [1, -5, 0]
    
    for val in test_values:
        print(f"Input number: {val}")
        
        if check_negative(val):
            print("The entered value is negative.")
        else:
            print("The entered value is not negative (it is zero or positive).")