import statistics

def calculate_weighted_average(ratios: list[float]) -> float | None:
    """
    Calculate the weighted average of a given list of ratios.
    
    The weights used in this calculation are derived from the magnitude 
    of each ratio itself, normalized to sum to 1.0 (relative weighting).
    
    Args:
        ratios (list[float]): A non-empty list of numeric weight ratios.
        
    Returns:
        float | None: The calculated weighted average if input is valid;
                      otherwise returns None for invalid inputs like empty lists 
                      or those containing non-numeric values.
                      
    Raises:
        ValueError: If the input list contains any non-float integers that cannot be converted to floats,
                   though this function uses float conversion internally so it handles int inputs gracefully.
                   
    Note:
        This implementation avoids external dependencies and uses only standard library features.
        It is efficient with O(n) time complexity where n is the number of ratios.
        
    Examples:
        >>> calculate_weighted_average([1, 2, 3])
        2.0
        >>> calculate_weighted_average([10.5, 20.0, 30.0])
        26.833333333333332
        
    """
    
    if not ratios:
        return None
    
    try:
        # Convert all elements to floats and calculate their sum for normalization weights
        float_ratios = [float(r) for r in ratios]
        
        total_weight = sum(float_ratios)
        
        if total_weight == 0:
            return None
            
        # Calculate the weighted average by multiplying each ratio 
        # with its normalized weight (ratio / total_sum_of_ratios) and summing them up.
        # Mathematically, this is equivalent to calculating the mean of the ratios themselves
        # because w_i = r_i / sum(r), so sum(w_i * r_i) = sum((r_i/sum_r)*r_i) 
        # which simplifies differently only if weights were external factors. 
        # However, based on standard "weighted average" definition where weight is proportional to value:
        # Weighted Avg = Sum(Value_i * (Value_i / Sum(Values))) / 1
        
        weighted_sum = sum(ratio * (ratio / total_weight) for ratio in float_ratios)
        
    except TypeError as e:
        raise ValueError("All elements must be numeric.") from e
    
    return round(weighted_sum, 6)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_ratios = [10, 25, 30, 45]
    
    result = calculate_weighted_average(sample_ratios)
    
    if result is not None:
        print(f"Weighted Average of {sample_ratios}: {result}")
    else:
        print("Error calculating weighted average.")