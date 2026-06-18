import sys

def check_negative(number: int) -> bool:
    """Check if a given integer is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input.
    # Testing cases: positive, zero, and negative numbers.
    
    test_cases = [15, -3, 0]

    for num in test_cases:
        is_negative = check_negative(num)
        
        if is_negative:
            print(f"The number {num} is negative.")
        else:
            print(f"The number {num} is not negative (it is zero or positive).")