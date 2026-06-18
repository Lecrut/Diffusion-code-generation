def is_divisible(dividend: int, divisor: int) -> bool:
    """Check if dividend is divisible by divisor (divisor must not be zero)."""
    return divisor != 0 and dividend % divisor == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    num1 = 24
    num2 = 8
    
    result = is_divisible(num1, num2)
    
    if result:
        print('True')
    else:
        print('False')