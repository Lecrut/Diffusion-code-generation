def check_difference(a: float | int, b: float | int) -> bool:
    """
    Returns True if two numerical values are different, False otherwise.

    Args:
        a (float|int): The first numerical value.
        b (float|int): The second numerical value.

    Returns:
        bool: True if a != b, else False.
    """
    return a != b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    
    result = check_difference(sample_a, sample_b)
    
    print(f"check_difference({sample_a}, {sample_b}) -> {result}")