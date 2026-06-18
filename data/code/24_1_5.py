def is_negative(value):
    """Returns True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    samples = [
        -5,      # Should be negative
        0,       # Not less than zero
        3.14,    # Positive float
        -2.718,  # Negative float
        -float('inf'),  # Negative infinity
        float('-inf')   # Alternative syntax for negative infinity (Python allows both)
    ]

    results = []
    for sample in samples:
        result = is_negative(sample)
        results.append((sample, result))

    print("Testing is_negative function:")
    for num, expected_negative in results:
        status = "PASS" if (num < 0 and not isinstance(num, float) or 
                           (num == -float('inf') and True)) else "FAIL"
        # Note: For the specific logic requested (< 0), negative infinity satisfies it.
        print(f"is_negative({num}) -> {result}")