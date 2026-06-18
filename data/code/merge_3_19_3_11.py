def is_divisible(first_num: int, second_num: int) -> bool:
    """Check if first_num is divisible by second_num without remainder."""
    return second_num != 0 and (first_num % second_num == 0)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    num1 = 24
    num2 = 6
    
    result = is_divisible(num1, num2)
    
    if result:
        print('True')
    else:
        print('False')