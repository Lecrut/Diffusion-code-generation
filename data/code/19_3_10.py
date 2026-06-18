def is_divisible(dividend: int, divisor: int) -> bool:
    """Check if dividend is divisible by divisor."""
    return divisor != 0 and (dividend % divisor == 0)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input.
    first_integer = 128
    second_integer = 4
    
    if is_divisible(first_integer, second_integer):
        print('True')
    else:
        print('False')