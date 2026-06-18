def calculate_dimension_ratio(length: float, width: float) -> float | None:
    """
    Calculates the ratio between two dimensions (length / width).
    
    Args:
        length (float): The numerator dimension. Must be positive.
        width (float): The denominator dimension. Must be positive.
        
    Returns:
        float or None: The calculated ratio if both inputs are valid, 
                      otherwise returns None to indicate an error condition.
                      
    Raises:
        ValueError: If either length or width is not a number or less than or equal to zero.
    
    Note: This function does not raise exceptions for invalid input but returns None instead,
          as per the requirement to handle constraints gracefully within the return value logic.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        # Handle non-numeric inputs by returning None
        return None
    
    try:
        length = float(length)
        width = float(width)
        
        if length <= 0 or width <= 0:
            return None
        
        return length / width
    except (TypeError, ValueError):
        # Handle conversion errors gracefully
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        {"length": 10.5, "width": 2},           # Should return 5.25
        {"length": 7, "width": 3},              # Should return ~2.333...
        {"length": -4, "width": 2},             # Invalid: negative length -> None
        {"length": 8, "width": 0},              # Invalid: zero width -> None
        {"length": "15", "width": 3},           # Invalid: non-numeric string -> None
    ]
    
    for i, test in enumerate(test_cases):
        length = test["length"]
        width = test["width"]
        
        result = calculate_dimension_ratio(length, width)
        
        print(f"Test Case {i + 1}:")
        if isinstance(result, float):
            print(f"Ratio: {result}")
        else:
            print("Result: None (Invalid input)")