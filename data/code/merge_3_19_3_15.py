def check_divisibility(first_int: int, second_int: int) -> bool:
    """Check if first_int is divisible by second_int."""
    return second_int != 0 and first_int % second_int == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed).
    val1 = 20
    val2 = 4

    result = check_divisibility(val1, val2)
    
    if result:
        print('True')
    else:
        print('False')