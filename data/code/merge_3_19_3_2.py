def check_divisibility(first_int: int, second_int: int) -> bool:
    """Check if first_int is divisible by second_int (second_int != 0)."""
    return second_int != 0 and first_int % second_int == 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    val1 = 20
    val2 = 4
    
    result = check_divisibility(val1, val2)
    
    if result:
        print('True')
    else:
        print('False')