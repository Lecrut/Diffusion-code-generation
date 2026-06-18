def check_zero(value):
    """Check if a numeric value is zero."""
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [0, -5, 3.14]

    for num in samples:
        result = check_zero(num)
        
        if isinstance(num, int):
            print(f"Integer {num} is {'zero' if result else 'not zero'}")
        elif isinstance(num, float):
            # Treat floats as non-zero unless they are exactly 0.0
            print(f"Float {num} is {'zero' if num == 0 else 'not zero'}")