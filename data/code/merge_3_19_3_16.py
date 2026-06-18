def check_divisibility(first_int: int, second_int: int) -> bool:
    """Check if first_int is divisible by second_int (second_int != 0)."""
    return second_int != 0 and first_int % second_int == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    a = 10
    b = 2
    
    if check_divisibility(a, b):
        print('True')
    else:
        print('False')