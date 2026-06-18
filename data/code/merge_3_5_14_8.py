def length_difference(len_a: int, len_b: int) -> int:
    """Returns the absolute difference between two lengths."""
    return (len_a - len_b) if len_a >= len_b else (len_b - len_a)

if __name__ == '__main__':
    sample_len1 = 50
    sample_len2 = 30
    result = length_difference(sample_len1, sample_len2)
    print(result)