def is_greater(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise returns False.

    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_a = 10.5
    sample_b = 20

    result = is_greater(sample_a, sample_b)
    
    print(f"Testing: {sample_a} > {sample_b}")
    print(f"Result: {result}")