def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float|int): The first value to compare.
        b (float|int): The second value to compare.
        
    Returns:
        bool: Result of the comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases running without external input or files
    result1 = is_greater(5, 3)
    print(f"5 > 3 -> {result1}")

    result2 = is_greater("hello", "hi")  # String comparison works lexicographically in Python
    print(f"'hello' > 'hi' -> {result2}")

    result3 = is_greater(0.9, 0.8)
    print(f"0.9 > 0.8 -> {result3}")