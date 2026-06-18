def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different, False otherwise.

    Args:
        a (float): First numerical value.
        b (float): Second numerical value.

    Returns:
        bool: True if a != b, else False.
    """
    return a != b

if __name__ == '__main__':
    sample1 = 5.0
    sample2 = 7.3
    result = check_difference(sample1, sample2)
    print(result)  # Expected output: True

    sample3 = 4.0
    sample4 = 4.0
    result2 = check_difference(sample3, sample4)
    print(result2)  # Expected output: False