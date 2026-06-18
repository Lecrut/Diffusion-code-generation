def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculates the ratio of two given lengths (length_a / length_b).
    
    Parameters:
        length_a (float): The numerator length.
        length_b (float): The denominator length.
        
    Returns:
        float or None: The calculated ratio if successful, otherwise None 
                      in case of division by zero.
    """
    try:
        return length_a / length_b
    except ZeroDivisionError:
        # Gracefully handle the case where dividing by zero occurs
        print("Error: Division by zero is not allowed.")
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    length_a = 10.5
    length_b = 2.3

    ratio_result = calculate_length_ratio(length_a, length_b)
    
    if ratio_result is not None:
        print(f"The ratio of {length_a} to {length_b} is: {ratio_result}")
    else:
        print("Calculation failed due to division by zero.")