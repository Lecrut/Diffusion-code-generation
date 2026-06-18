def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculate the absolute difference between two weight values.

    Parameters:
        w1 (float): First weight value.
        w2 (float): Second weight value.

    Returns:
        float: The absolute difference between w1 and w2.
    
    Optimization Note:
        Uses direct subtraction which is O(1) time complexity, 
        appropriate for floating-point arithmetic in Python's native types.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external input or files are needed
    weight_one = 50.75
    weight_two = 48.30
    
    result = calculate_weight_difference(weight_one, weight_two)
    
    print(f"Difference between {weight_one} and {weight_two}: {result}")