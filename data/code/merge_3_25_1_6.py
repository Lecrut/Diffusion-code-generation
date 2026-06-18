def is_zero(value):
    """Returns True if value is zero (0), False otherwise."""
    return value == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [0, -1.5e-24, float('inf'), '0', [], {}, None]

    for sample in samples:
        result = is_zero(sample)
        print(f"is_zero({sample!r}) = {result}")