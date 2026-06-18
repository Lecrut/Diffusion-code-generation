def is_zero(value):
    """Returns True if value is exactly zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    samples = [
        (1 + 2),           # Should be False
        (-4.5 / -3 * 9 + 8) * 7 + 1,  # Non-zero result of arithmetic
        float(0),          # Zero as float
        int(0 * 10),       # Explicitly zero
    ]

    for i_val in samples:
        print(f"Input: {i_val}, is_zero: {is_zero(i_val)}")