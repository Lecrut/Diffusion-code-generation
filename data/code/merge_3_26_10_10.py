def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    
    result = is_greater(sample_a, sample_b)
    
    print(f"is_greater({sample_a}, {sample_b}) = {result}")