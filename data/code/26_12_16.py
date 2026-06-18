def validate_number(user_input):
    """Check if the input is a valid integer."""
    try:
        return int(float(user_input))
    except (ValueError, TypeError):
        raise ValueError("Invalid number.")

def compare_numbers(num1, num2):
    """Compare two numbers and print which one is greater."""
    result = "The first number ({}) is greater than the second number ({}).".format(num1, num2) if num1 > num2 else \
             "The first number ({}) is not greater than the second number ({}).".format(num1, num2)
    print(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or command-line arguments are required.
    sample_value_1 = "5"
    sample_value_2 = "3"

    try:
        num1 = validate_number(sample_value_1)
        num2 = validate_number(sample_value_2)
        
        # Test and print comparison result using an if statement
        compare_numbers(num1, num2)
        
    except ValueError as e:
        print("Error:", str(e))