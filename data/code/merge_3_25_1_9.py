def is_zero(number):
    """Returns True if number is zero, False otherwise."""
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or command-line arguments
    samples = [0.0, 1, -5, "0", 3.14]

    for val in samples:
        try:
            result = is_zero(val)
            print(f"is_zero({val!r}) == {result}")
        except TypeError as e:
            # Non-numeric or invalid types will raise an exception during comparison, handled gracefully here
            print(f"Error testing with {val!r}: {e}")