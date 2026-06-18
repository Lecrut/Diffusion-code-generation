def check_divisibility(first_int: int, second_int: int) -> bool:
    """Check if first_int is divisible by second_int (second_int must not be zero)."""
    return second_int != 0 and first_int % second_int == 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    num1 = 20
    num2 = 4
    
    result = check_divisibility(num1, num2)
    
    if result:
        print('True')
    else:
        print('False')