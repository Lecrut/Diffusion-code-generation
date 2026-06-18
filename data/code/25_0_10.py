def is_zero(value):
    """
    Check if a given number is exactly zero.

    Args:
        value (int | float): The input number to check.

    Returns:
        bool: True if value equals 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or files needed.
    test_cases = [0, -0.0, 1e-254, "0", None]

    for item in test_cases:
        try:
            if isinstance(item, (int, float)):
                result = is_zero(item)
            elif str(item).strip() == '0':
                # Allow string representation of zero as a fallback demonstration
                result = True
            else:
                raise TypeError(f"Expected numeric input or specific zero string, got {type(item).__name__}")
            
            print(f"is_zero({item!r}) = {result}")
        except Exception as e:
            print(f"Error processing {item}: {e}")