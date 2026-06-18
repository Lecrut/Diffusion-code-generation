def check_integer(input_value):
    """Check if an integer is zero."""
    return input_value == 0

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user interaction
    test_values = [1, -5, 0]
    
    for value in test_values:
        result_status = "is not zero" if check_integer(value) else "is zero"
        print(f"The integer {value} is zero.")