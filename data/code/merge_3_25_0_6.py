def is_zero(number):
    """Check if a given number is exactly zero."""
    return number == 0

if __name__ == '__main__':
    test_values = [0, -1, 1, 0.0, float('inf'), None]
    
    for value in test_values:
        try:
            result = is_zero(value) if isinstance(value, (int, float)) else "Invalid type"
            print(f"is_zero({value}) = {result}")
        except Exception as e:
            print(f"is_zero({value}) raised an error: {e}")