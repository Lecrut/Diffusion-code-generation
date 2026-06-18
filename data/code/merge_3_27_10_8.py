def check_difference(a: float, b: float) -> bool:
    """Returns True if a is different from b, False otherwise."""
    return a != b

if __name__ == '__main__':
    sample_values = [1.0, 2.0]
    result = check_difference(sample_values[0], sample_values[1])
    print(result)