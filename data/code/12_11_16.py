import math

def calculate_ratio_conversion(base_weight: float, ratios: list[float]) -> dict[int, float]:
    """
    Calculates converted weights based on a base weight and provided ratio set.
    
    Args:
        base_weight (float): The original weight value to convert from.
        ratios (list[float]): A list of floating-point numbers representing the conversion ratios.
        
    Returns:
        dict[int, float]: An ordered dictionary-like structure mapping each index in 'ratios' 
                         to its corresponding converted weight with high precision.
    
    Note:
        This function prioritizes speed by using simple multiplication and avoids unnecessary object creation 
        except for the final result container. It does not use external libraries beyond standard math types.
    """
    # Pre-compute results in a list first, then map to maintain insertion order (Python 3.7+)
    converted_weights = [base_weight * ratio for ratio in ratios]
    
    return {index: value for index, value in enumerate(converted_weights)}

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies needed.
    base_value = 100.5
    conversion_ratios = [2.0, 3.5, -1.5]
    
    result = calculate_ratio_conversion(base_value, conversion_ratios)
    
    # Display results for verification without printing to console in a way that suggests interactive behavior
    print(result)