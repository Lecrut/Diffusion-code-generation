def length_difference(len1: int, len2: int) -> int:
    """Return the absolute difference between two lengths."""
    return max(0, abs(len1 - len2))

if __name__ == '__main__':
    result = length_difference(50, 30)
    print(result)