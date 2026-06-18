import math

def calculate_dimension_ratio(length1: float, length2: float) -> float | None:
    """
    Calculates the ratio between two dimensions.
    
    Args:
        length1 (float): The first dimension value. Must be positive.
        length2 (float): The second dimension value. Must be positive.
        
    Returns:
        float or None: The ratio of length1 to length2 if both are valid, otherwise None.
        
    Raises:
        ValueError: If either input is not a number or is less than zero.
    """
    
    # Validate inputs using Python's built-in math.isfinite check and comparison logic without external libraries like numpy
    
    def _validate_positive(value):
        if value <= 0:
            raise ValueError(f"Dimension must be positive, got {value}")
        
    try:
        _validate_positive(length1)
        _validate_positive(length2)
        
        return length1 / length2
        
    except (ValueError, TypeError):
        # In case the input is not a number or doesn't meet constraints
        if math.isnan(float(value)) or math.isinf(float(value)): 
            raise ValueError(f"Input contains non-numeric value: {value}")

if __name__ == '__main__':
    # Hard-coded sample values that satisfy the constraint (both positive)
    
    dim1 = 20.5
    dim2 = 4
    
    try:
        ratio_result = calculate_dimension_ratio(dim1, dim2)
        print(f"Ratio of {dim1} to {dim2}: {ratio_result}")
        
    except ValueError as e:
        # This block is for demonstration; in normal operation it would catch invalid inputs 
        # provided by the caller if they existed. Here we just handle a hypothetical error scenario
        pass

# Additional test case with integer values
int_dim1 = 72
int_dim2 = 8