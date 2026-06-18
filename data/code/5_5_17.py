import math

def compare_length_lists(list1: list[float], list2: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine max/min lengths 
    and reports the overall range difference across both combined sets.
    
    Args:
        list1 (list[float]): First list of numerical values representing lengths.
        list2 (list[float]): Second list of numerical values representing lengths.
        
    Returns:
        dict: A dictionary containing 'combined_max', 'combined_min', and 'range_difference'.
              Raises ValueError if lists are empty or contain non-numeric data.
    """
    
    # Validate inputs for emptiness
    if not isinstance(list1, list) or len(list1) == 0:
        raise ValueError("First argument must be a non-empty list.")
    if not isinstance(list2, list) or len(list2) == 0:
        raise ValueError("Second argument must be a non-empty list.")
    
    # Validate inputs for numeric content and combine lists
    combined = []
    try:
        for val in list1 + list2:
            float(val)  # Attempt conversion to ensure it's numeric
            combined.append(float(val))
    except (ValueError, TypeError):
        raise ValueError("All elements in both lists must be convertible to numbers.")

    if len(combined) == 0:
        return {
            'combined_max': None, 
            'combined_min': None, 
            'range_difference': math.nan
        }

    combined_max = max(combined)
    combined_min = min(combined)
    
    # Calculate range difference as the span of values found in both lists together
    range_difference = combined_max - combined_min
    
    return {
        'combined_max': combined_max, 
        'combined_min': combined_min, 
        'range_difference': range_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    list_a = [10.5, 23.4, 8.9]
    list_b = [15.2, 7.6, 24.1]

    result = compare_length_lists(list_a, list_b)
    
    print(f"Combined Maximum Length: {result['combined_max']}")
    print(f"Combined Minimum Length: {result['combined_min']}")
    print(f"Overall Range Difference: {result['range_difference']:.2f}")