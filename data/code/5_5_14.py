import statistics

def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine maximum and minimum lengths 
    present in both lists combined, then calculates the overall range difference.
    
    Args:
        list_a (list[float]): First list of numerical values representing lengths.
        list_b (list[float]): Second list of numerical values representing lengths.
        
    Returns:
        dict[str, float]: A dictionary containing 'max_length', 'min_length', and 
                         'range_difference'. If either input is empty or contains non-numeric 
                         data that cannot be converted to float, a ValueError is raised.
    
    Raises:
        ValueError: If inputs are not lists of numeric values (floats).
    """
    # Validate inputs
    if list_a == [] and list_b == []:
        raise ValueError("At least one input list must contain data.")

    combined = [x for x in list_a + list_b]
    
    try:
        max_length = float(max(combined))
        min_length = float(min(combined))
        
        range_difference = abs(max_length - min_length)
        
        return {
            'max_length': max_length,
            'min_length': min_length,
            'range_difference': range_difference
        }
    except ValueError:
        raise ValueError("All elements in both lists must be numeric (float).")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    
    list_a = [10.5, 20.3, 15.7]
    list_b = [8.9, 22.4, 16.1]

    result = compare_length_lists(list_a, list_b)

    print(f"Maximum length: {result['max_length']}")
    print(f"Minimum length: {result['min_length']}")
    print(f"Overall range difference: {result['range_difference']:.2f}")