import sys

def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations instead of modulo.
    
    The least significant bit (LSB) represents powers of 2 (1, 2, 4...). 
    If the LSB is set to 1, the number is odd; otherwise, it is even.
    This avoids division which involves more complex CPU instructions.
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access
    test_values = [0, 1, -1, 2, 3, -5, 10**6]
    
    for val in test_values:
        result = is_odd_bitwise(val)
        print(f"Number: {val}, Is Odd (Bitwise): {result}")