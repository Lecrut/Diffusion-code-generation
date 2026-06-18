def is_zero(value):
    """
    Checks if a given input number is exactly zero.

    Args:
        value (int | float): The numerical value to check against 0.

    Returns:
        bool: True if the value equals exactly 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, -123456789.0, "0", True, False]

    results = []
    for num in test_cases:
        try:
            result = is_zero(num)
            results.append(f"Input {num!r} -> {result}")
        except TypeError as e:
            # Handle cases where non-numeric types are passed (like string "0")
            results.append(f"Input {num!r} raised an error during type check: {e}. It is likely not a numeric zero.")

    for result in results:
        print(result)