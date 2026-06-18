def is_negative(value: float) -> bool:
    """Returns True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [-5.123, -42, 0, 0.0, 1e-9, float('-inf')]
    
    for num in samples:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")