import math

def validate_positive_number(user_input):
    """Validates that the input is a positive number."""
    try:
        value = float(user_input)
        if value <= 0:
            raise ValueError("Input must be a positive number.")
        return value
    except ValueError as e:
        # Re-raise with clearer context or handle specific exceptions here
        raise

def calculate_ratio(length_a, length_b):
    """Calculates the ratio of two lengths."""
    if length_b == 0:
        raise ZeroDivisionError("Second length cannot be zero.")
    return length_a / length_b

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    SAMPLE_LENGTH_A = 120.5
    SAMPLE_LENGTH_B = 48
    
    try:
        ratio_result = calculate_ratio(SAMPLE_LENGTH_A, SAMPLE_LENGTH_B)
        
        print("=" * 30)
        print("Ratio Calculation Result")
        print("=" * 30)
        print(f"Length A (First): {SAMPLE_LENGTH_A} units")
        print(f"Length B (Second): {SAMPLE_LENGTH_B} units")
        print("-" * 30)
        
        # Format the ratio to a reasonable number of decimal places for clarity
        formatted_ratio = f"{ratio_result:.4f}"
        print(f"Their Ratio: {formatted_ratio}")
        
    except ValueError as ve:
        print(f"Input Error: {ve}. Please ensure inputs are positive numbers.")
    except ZeroDivisionError as zde:
        print(f"Mathematical Error: {zde}. The second length cannot be zero.")