def is_greater(a: float | int, b: float | int) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 7
    result = is_greater(sample_a, sample_b)
    print(f"is_greater({sample_a}, {sample_b}) = {result}")