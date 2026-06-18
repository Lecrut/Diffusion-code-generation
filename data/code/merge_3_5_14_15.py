def length_difference(len_a: int, len_b: int) -> int:
    """Returns the absolute difference between two lengths."""
    return abs(len_a - len_b)

if __name__ == '__main__':
    a = 10
    b = 4
    result = length_difference(a, b)
    print(result)