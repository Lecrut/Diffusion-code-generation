def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -123456789, 0.0, "0", None]
    for case in test_cases:
        try:
            result = is_zero(case) if isinstance(case, (int, float)) else False
            print(f"is_zero({case!r}) -> {result}")
        except Exception as e:
            # Handle non-numeric types gracefully by returning False or raising specific error logic here if needed.
            # Since the task asks for a numerical argument check but sample might include edge cases, we handle type safety implicitly via try/except in main block demonstration.
            print(f"is_zero({case!r}) -> Error handling: {e}")