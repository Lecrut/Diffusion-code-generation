def handle_input(value):
    """Check if a numeric value is zero."""
    return value == 0

if __name__ == '__main__':
    sample_values = [0, -5, 3]
    
    for val in sample_values:
        # Simulate user input by using the hard-coded values directly.
        # Since interactive prompts and sys.stdin are forbidden.
        is_zero = handle_input(val)
        
        if not isinstance(val, int):
            print(f"{val} was rejected as non-integer.")
        elif val == 0:
            print(f"The value {val} is zero.")
        else:
            print(f"The value {val} is not zero.")