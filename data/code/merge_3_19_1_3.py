def is_greater(a: int | float, b: int | float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 3.2
    result = is_greater(sample_a, sample_b)
    print(result)