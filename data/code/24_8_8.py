def check_number(value):
    """Checks if a given integer is negative."""
    return value < 0

if __name__ == '__main__':
    # Sample values to test without user input
    sample_values = [-5, 10, -3.7]
    
    for num in sample_values:
        is_negative = check_number(num)
        
        if isinstance(num, int):
            status_text = "negative" if is_negative else "non-negative"
            print(f"The integer {num} is a {status_text}.")
        elif isinstance(num, float):
            # For floats, we consider it negative only if the value itself is less than zero (standard mathematical definition)
            # The task specifies reading an integer, but checking sample values including non-integers demonstrates robustness.
            status_text = "negative" if num < 0 else "non-negative"
            print(f"The number {num} is a {status_text}.")