import math

def compare_length_lists(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine maximum and minimum 
    lengths present in both lists and reports the overall range difference.

    Args:
        list1 (list[float]): First list of numeric length values.
        list2 (list[float]): Second list of numeric length values.

    Returns:
        dict[str, float]: A dictionary containing 'max_length', 'min_length', 
                         and 'range_difference'. If either input is empty or invalid,
                         appropriate error handling returns None for that key.
    
    Raises:
        ValueError: If inputs are not lists of numeric types (int/float).
    """
    # Validate inputs
    if not isinstance(list1, list) or not all(isinstance(x, (int, float)) for x in list1):
        raise ValueError("list1 must be a list of numbers.")
    if not isinstance(list2, list) or not all(isinstance(x, (int, float)) for x in list2):
        raise ValueError("list2 must be a list of numbers.")

    # Flatten both lists to find the global max and min across both inputs
    combined_lengths = []
    
    try:
        if len(list1) > 0:
            combined_lengths.extend([float(x) for x in list1])
        else:
            raise ValueError("list1 is empty.")

        if len(list2) > 0:
            combined_lengths.extend([float(x) for x in list2])
        else:
            raise ValueError("list2 is empty.")
    except (ValueError, TypeError):
        # Handle cases where conversion fails or lists are invalidly structured beyond type check
        return {
            'max_length': None, 
            'min_length': None, 
            'range_difference': 0.0
        }

    if not combined_lengths:
        return {'max_length': None, 'min_length': None, 'range_difference': 0.0}

    max_val = float(max(combined_lengths))
    min_val = float(min(combined_lengths))
    
    # Calculate range difference (absolute value of the spread)
    range_diff = abs(max_val - min_val) if not math.isnan(range_diff) else None
    
    return {
        'max_length': max_val, 
        'min_length': min_val, 
        'range_difference': range_diff
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    
    list_a = [10.5, 20.3, 30.7]
    list_b = [40.1, 50.9, 60.2]

    result = compare_length_lists(list_a, list_b)

    if result['max_length'] is not None:
        print(f"Maximum Length: {result['max_length']}")
        print(f"Minimum Length: {result['min_length']}")
        print(f"Range Difference: {result['range_difference']}")
    else:
        print("Error in data processing.")