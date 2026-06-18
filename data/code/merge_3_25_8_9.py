def is_zero_number(value: str) -> bool:
    """
    Attempts to evaluate a user-provided string as a number.
    
    Returns True if the resulting numeric value is zero, False otherwise.
    Raises ValueError or TypeError on invalid input formats.
    """
    try:
        num = float(value.strip())
        return num == 0.0
    except (ValueError, TypeError):
        # Handle cases where conversion fails or non-numeric string provided
        raise

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        "0",          # Should return True
        "-0.0",       # Should return True (float equivalent)
        "  0 ",       # Whitespace padded, should return True
        "3.14",       # Non-zero number, should return False
        "abc",        # Invalid string, will raise exception
        "",           # Empty string, will raise ValueError
    ]

    for sample in samples:
        try:
            result = is_zero_number(sample)
            print(f"Input '{sample}' -> Result: {result}")
        except Exception as e:
            print(f"Input '{sample}' raised an exception: {type(e).__name__}: {e}")