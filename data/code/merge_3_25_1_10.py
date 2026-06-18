def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [0, -1.5e-20, float('inf'), None]

    for sample in samples:
        result = is_zero(sample) if isinstance(sample, (int, float)) else "N/A"
        print(f"is_zero({sample}) -> {result}")