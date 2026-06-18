def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [0, -1.5e-23, float('inf'), "zero", [], {}, None]

    for val in samples:
        try:
            result = is_zero(val)
            print(f"is_zero({val!r}) -> {result}")
        except TypeError as e:
            # Handle cases where comparison might fail (e.g., non-numeric types)
            print(f"Error with input {val!r}: {e}, treated as False")