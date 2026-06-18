def is_even(number: int) -> bool:
    """
    Returns True if number is even, False otherwise.
    
    Uses bitwise AND operation which is generally faster than modulo 
    for large integers in Python due to lower CPU instruction overhead.
    An integer n is even if its least significant bit is 0 (n & 1 == 0).
    """
    return not number % 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [0, -5, 42, -8, 1]
    
    for sample in samples:
        result = is_even(sample)
        print(f"is_even({sample}) = {result}")