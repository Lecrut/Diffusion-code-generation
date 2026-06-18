def compare_large_integers(a: int, b: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python handles arbitrarily large integers natively using arbitrary-precision arithmetic,
    so standard comparison operators are safe and efficient for this purpose.
    
    Args:
        a (int): First integer to compare.
        b (int): Second integer to compare.
        
    Returns:
        str: 'greater' if a > b, 'less' if a < b, or 'equal' if a == b.
    """
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"

if __name__ == '__main__':
    # Hard-coded sample values representing potentially large integers
    num1 = 2**50 + 3 ** 49 - 7 * (8 ** 6)
    num2 = 10 ** 100
    
    result = compare_large_integers(num1, num2)
    
    if __name__ == '__main__':
        print(f"Comparison of {num1} and {num2}:")
        print(result)