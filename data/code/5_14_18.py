def get_difference_length(len_a: int, len_b: int) -> int:
    """Returns the absolute difference between two lengths."""
    return abs(len_a - len_b)

if __name__ == '__main__':
    result = get_difference_length(10, 4)
    print(result)