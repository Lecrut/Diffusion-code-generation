import sys

def compare_integers(a: int, b: int) -> int:
    """
    Compares two integers and returns -1 if a < b, 0 if a == b, or 1 if a > b.
    
    Although Python automatically handles arbitrarily large integers without overflow,
    this function ensures the comparison logic is explicit and clean for any integer size.

    Args:
        a (int): The first integer to compare.
        b (int): The second integer to compare.

    Returns:
        int: -1 if a < b, 0 if a == b, or 1 if a > b.
    """
    return (-1 if a < b else (1 if a > b else 0))

if __name__ == '__main__':
    # Sample values for testing the compare_integers function without user input.
    sample_a = 42
    sample_b = -98765432109876543210
    
    result = compare_integers(sample_a, sample_b)
    
    if result == -1:
        print(f"{sample_a} is less than {sample_b}")
    elif result == 0:
        print(f"{sample_a} equals {sample_b}")
    else:
        print(f"{sample_a} is greater than {sample_b}")

    # Additional test case with large positive integers to ensure no overflow issues.
    sample_large1 = (2 ** 53) + 100
    sample_large2 = (2 ** 64) * 7
    
    result_large = compare_integers(sample_large1, sample_large2)
    
    if result_large == -1:
        print(f"{sample_large1} is less than {sample_large2}")