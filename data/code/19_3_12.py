def check_divisibility(num1: int, num2: int) -> bool:
    """Check if num1 is divisible by num2 (num2 must not be zero)."""
    return num2 != 0 and num1 % num2 == 0

if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 5
    
    result = check_divisibility(sample_num1, sample_num2)
    
    if result:
        print('True')
    else:
        print('False')