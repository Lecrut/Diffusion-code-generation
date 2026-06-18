def is_zero(number) -> bool:
    """Check if a given number is exactly zero."""
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [0, -1.5e-38, float('inf'), "0", "", [], {}]

    for value in samples:
        try:
            numeric_value = complex(value) if not isinstance(value, (int, float)) else value
            result = is_zero(numeric_value.real if hasattr(numeric_value, 'real') and hasattr(numeric_value, 'imag') else numeric_value)
            print(f"Number {value} ('{numeric_value}') is zero: {result}")
        except Exception as e:
            print(f"Error processing sample '{value}': {e}")