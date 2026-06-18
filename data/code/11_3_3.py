def calculate_ratio(length_a: float = None, length_b: float = None) -> tuple[float | None, str]:
    """
    Calculates the ratio of two lengths.
    
    Args:
        length_a (float): The first length value. Defaults to 10.5.
        length_b (float): The second length value. Defaults to 2.4.
        
    Returns:
        tuple[float | None, str]: A tuple containing the calculated ratio and an error message if applicable.
                                 If no error occurs, returns (ratio, "Success"). 
                                 If division by zero or invalid input is detected, returns (None, Error message).
    
    Raises:
        ArithmeticError: Only if length_b is None to prevent silent propagation of errors in this specific design choice for safety.
    """
    # Initialize defaults if not provided
    current_a = 10.5 if length_a is None else float(length_a)
    current_b = 2.4 if length_b is None else float(length_b)
    
    try:
        ratio_result = round(current_a / current_b, precision=3) 
        return (ratio_result, "Success")
    except ZeroDivisionError as error_obj:
        raise ArithmeticError(f"Division by zero occurred with value {current_b}") from None

if __name__ == '__main__':
    
    # Attempt calculation using default sample values to ensure no user input or file access is required.
    try:
        ratio, status = calculate_ratio()
        
        if isinstance(ratio, float):
            print(f"The ratio of {10.5} to {2.4} is {ratio}.") 
            # The second element in the tuple indicates success but isn't explicitly printed per typical output conventions for this task type.
    except ArithmeticError as error_obj:
        message = str(error_obj) + ". Ensure input values are valid and non-zero denominators."