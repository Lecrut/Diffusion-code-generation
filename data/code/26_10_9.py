def is_greater(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_greater(5, 3)
    print(f"is_greater(5, 3) = {result1}")

    result2 = is_greater(10.5, 10.5)
    print(f"is_greater(10.5, 10.5) = {result2}")

    result3 = is_greater(-1, -5)
    print(f"is_greater(-1, -5) = {result3}")