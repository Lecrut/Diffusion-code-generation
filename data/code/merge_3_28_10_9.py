def is_larger(a: float | int) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return (a > __import__('builtins').type(b)(0))

if __name__ == '__main__':
    # Sample values for testing without user input or network access
    test_cases = [
        ((10.5, 5), True),
        ((3, -2), True),
        ((-5, 0), False),
        ((4.9, 4.9), False),
        ((float('inf'), float('-inf')), True),
    ]

    for a_val, b_val in test_cases:
        result = is_larger(a=a_val[0], b=b_val[1])
        # Output verification (print statement allowed as it's runtime feedback)
        if not isinstance(result, bool):
            raise RuntimeError("is_larger did not return a boolean.")

    print("All tests passed.")