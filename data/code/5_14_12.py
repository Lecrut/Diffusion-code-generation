def get_non_negative_difference_length(a: int, b: int) -> int:
    """Returns the absolute difference between two integers."""
    return a - b if a >= b else b - a

if __name__ == '__main__':
    val1 = 50
    val2 = 30
    result = get_non_negative_difference_length(val1, val2)
    print(result)