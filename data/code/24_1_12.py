def is_negative(value):
    """
    Returns True if value < 0, False otherwise.
    
    Args:
        value (number): A numerical input to check against zero.
        
    Returns:
        bool: True if the number is negative, False otherwise.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or external dependencies
    test_cases = [
        -5,
        -3.14,
        0,
        2,
        float('-inf'),
        float('inf')
    ]

    print("Testing is_negative function:")
    for num in test_cases:
        result = is_negative(num)
        status = "Negative" if result else "Non-negative"
        print(f"{num}: {status}")