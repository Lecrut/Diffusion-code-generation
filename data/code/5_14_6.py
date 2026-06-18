def length_difference(len_a: int, len_b: int) -> int:
    """Return the absolute difference between two lengths."""
    return abs(len_a - len_b)

if __name__ == '__main__':
    result = length_difference(10, 4)
    print(result)