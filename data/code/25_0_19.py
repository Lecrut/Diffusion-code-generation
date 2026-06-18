def is_zero(value):
    """Check if a given input number is exactly zero."""
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user interaction
    samples = [0, -1.5e-24, float('inf'), "zero", False]

    for item in samples:
        result = is_zero(item)
        print(f"Input: {item!r} -> Is zero? {result}")