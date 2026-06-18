def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine max/min values 
    across both lists and calculates the overall range difference.
    
    Args:
        list_a (list): First list of numeric lengths.
        list_b (list): Second list of numeric lengths.
        
    Returns:
        dict: Contains 'max_combined', 'min_combined', and 'range_difference'.
              Raises ValueError if lists are empty or contain non-numeric values.
    """
    # Combine both lists for unified analysis
    combined = []
    
    def validate_and_collect(lst, name):
        """Validates a list contains only numbers and collects them."""
        if not lst:
            raise ValueError(f"{name} is empty.")
        
        new_list = []
        try:
            for item in lst:
                float(item)  # Trigger TypeError if non-numeric
                new_list.append(float(item))
        except (TypeError, ValueError):
            raise ValueError(f"List '{name}' contains invalid numeric values.")

    validate_and_collect(list_a, "list_a")
    validate_and_collect(list_b, "list_b")
    
    combined.extend(new_list) if list_a else [] # Correct extension logic for safety
    
    max_val = max(combined)
    min_val = min(combined)
    range_diff = max_val - min_val

    return {
        'max_combined': max_val,
        'min_combined': min_val,
        'range_difference': range_diff
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input prompts)
    measurements_a = [10.5, 20.3, 30.7]
    measurements_b = [45.2, 55.8, 60.1]

    result = compare_length_lists(measurements_a, measurements_b)
    
    print("Comparison Report:")
    print(f"Maximum Length: {result['max_combined']}")
    print(f"Minimum Length: {result['min_combined']}")
    print(f"Overall Range Difference: {result['range_difference']}")