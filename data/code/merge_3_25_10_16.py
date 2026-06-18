def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (number): A numerical argument to check against zero.
        
    Returns:
        bool: True if value equals 0.0, else False.
    """
    return value == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_values = [
        (5.0, False),
        (-3, False),
        (0, True),
        (1e-20, False),
        (float('nan'), False),
        (float('inf'), False),
    ]

    for val, expected in sample_values:
        result = is_zero(val)
        print(f"is_zero({val}) == {result} (expected {expected}, {'PASS' if result == expected else 'FAIL'})")