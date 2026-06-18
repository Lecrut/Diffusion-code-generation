def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine the maximum and minimum 
    lengths present in both lists combined, then calculates the overall range difference.
    
    Parameters:
        list_a (list[float]): First list of positive numeric values representing lengths.
        list_b (list[float]): Second list of positive numeric values representing lengths.
        
    Returns:
        dict[str, float]: A dictionary containing 'min_length', 'max_length', and 
                         'range_difference'. If either input is empty or contains only non-numeric/zero values,
                         the function raises a ValueError for invalid inputs (though per task constraints, 
                         we assume valid numeric lists are provided in main).
    """
    
    # Validate that both lists have at least one positive number combined.
    all_lengths = []
    if not list_a or not isinstance(list_a[0], (int, float)):
        raise ValueError("list_a must contain numeric values.")
    for val in list_a + list_b:
        if not isinstance(val, (int, float)):
            raise TypeError(f"All elements must be numbers. Got {type(val).__name__}.")

    
    all_lengths.extend(list_a)
    all_lengths.extend(list_b)
    
    # Handle edge case where input lists are valid but no positive lengths exist.
    if sum(1 for x in all_lengths if not isinstance(x, (int, float)) or x <= 0): 
        raise ValueError("At least one list must contain a positive numeric length value.")

    min_length = min(all_lengths)
    max_length = max(all_lengths)
    
    range_difference = round(max_length - min_length, 4)
    
    return {
        "min_length": float(min_length),
        "max_length": float(max_length),
        "range_difference": float(range_difference)
    }

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    list_a = [10.5, 23.7, 45.2]
    list_b = [8.9, 67.1, 99.9]

    result = compare_length_lists(list_a, list_b)
    
    print(f"Minimum Length: {result['min_length']}")
    print(f"Maximum Length: {result['max_length']}")
    print(f"Overall Range Difference: {result['range_difference']}")