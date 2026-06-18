def check_divisibility(first_int: int, second_int: int) -> bool:
    """Check if first_int is divisible by second_int (second_int must not be zero)."""
    return second_int != 0 and first_int % second_int == 0

if __name__ == '__main__':
    sample_first = 10
    sample_second = 2
    
    result = check_divisibility(sample_first, sample_second)
    
    if result:
        print('True')
    else:
        print('False')