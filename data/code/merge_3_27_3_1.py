def check_difference(a: int | float = 10, b: int | float = 20) -> bool:
    """Check if 'a' is different from 'b'."""
    return a != b

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    result = check_difference(sample_a, sample_b)
    print(result)