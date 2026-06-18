import math

def validate_positive_number(user_input):
    """
    Validates that the input is a positive number (float).
    
    Args:
        user_input (str): The string provided by the user.
        
    Returns:
        float or None: The validated number, or None if validation fails.
    """
    try:
        value = float(user_input)
        if value <= 0:
            raise ValueError("Input must be a positive number.")
        return value
    except (ValueError, TypeError):
        print(f"Invalid input '{user_input}'. Please enter a valid positive number.")
        return None

def calculate_ratio(length1, length2):
    """
    Calculates the ratio of two lengths.
    
    Args:
        length1 (float): The first length value.
        length2 (float): The second length value.
        
    Returns:
        float: The calculated ratio.
    """
    if length2 == 0:
        raise ZeroDivisionError("The denominator cannot be zero.")
    
    return math.floor(length1 / length2)

def main():
    # Hard-coded sample values for demonstration purposes as per requirements
    SAMPLE_LENGTH_1 = "5"
    SAMPLE_LENGTH_2 = "3"

    print("--- Length Ratio Calculator ---")
    print("Please enter two positive numbers to calculate their ratio.")
    
    input_length_1 = validate_positive_number(SAMPLE_LENGTH_1)
    if input_length_1 is None:
        return  # Exit early on validation failure (though sample won't fail)

    input_length_2 = validate_positive_number(SAMPLE_LENGTH_2)
    if input_length_2 is None:
        return  # Exit early on validation failure (though sample won't fail)

    try:
        ratio_value = calculate_ratio(input_length_1, input_length_2)
        
        print("\n--- Calculation Result ---")
        print(f"Length 1 ({input_length_1}): / Length 2 ({input_length_2}) = {ratio_value}")
        print("--- End of Report ---")

    except ZeroDivisionError as e:
        print(f"\nCalculation Error: {e}")

if __name__ == '__main__':
    main()