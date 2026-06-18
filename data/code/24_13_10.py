import sys

def check_number(n):
    """Check if a number is negative."""
    return n < 0

if __name__ == '__main__':
    # Sample values to test without user input
    sample_values = [-5, 10, -3.5]
    
    for val in sample_values:
        result = check_number(val)
        
        if result:
            print(f"Value {val} is negative.")
        else:
            print(f"Value {val} is not negative (it is non-negative).")