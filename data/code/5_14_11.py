def get_difference_length(l1: int, l2: int) -> int:
    """Returns the absolute difference between two length values."""
    return abs(l1 - l2)

if __name__ == '__main__':
    a = 50
    b = 30
    result = get_difference_length(a, b)
    print(result)