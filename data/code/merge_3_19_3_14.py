def is_divisible(a: int, b: int) -> bool:
    """Check if integer a is divisible by non-zero integer b."""
    return b != 0 and (a % b == 0)

if __name__ == '__main__':
    val1 = 25
    val2 = 5
    
    result = is_divisible(val1, val2)
    
    if result:
        print('True')
    else:
        print('False')