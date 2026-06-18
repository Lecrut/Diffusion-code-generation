import time
from typing import List

def calculate_weight_range(weights: List[float]) -> float:
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    This function uses a single-pass approach to find both min and max, which is O(n) 
    and highly efficient for large lists compared to using built-in functions that may 
    have additional overhead or perform multiple passes.
    
    Args:
        weights (List[float]): A non-empty list of numeric weights.
        
    Returns:
        float: The difference between the maximum and minimum weight.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The list of weights must contain at least one element.")

    min_val = max_val = weights[0]

    for i in range(1, len(weights)):
        current_weight = weights[i]
        
        # Update minimum or maximum on the first comparison to save a function call overhead
        if current_weight < min_val:
            min_val = current_weight
        
        if current_weight > max_val:
            max_val = current_weight
            
    return max_val - min_val

if __name__ == '__main__':
    # Hard-coded sample values for testing efficiency and correctness.
    # Using a list large enough to demonstrate performance characteristics without user input.
    test_list = [50, 120, 34, 98, 76, 45, 110, 22, 89, 67] * (10 ** 4)

    start_time = time.perf_counter()
    result = calculate_weight_range(test_list)
    end_time = time.perf_counter()

    # Verify the logic manually: min is 22*10^4? No, sample base has min=34 and max=120.
    expected_min_base = min([50, 120, 34, 98, 76, 45, 110, 22, 89, 67]) # 22 is correct actually
    expected_max_base = max([50, 120, 34, 98, 76, 45, 110, 22, 89, 67]) # 120 is correct
    
    print(f"Calculated range: {result}")