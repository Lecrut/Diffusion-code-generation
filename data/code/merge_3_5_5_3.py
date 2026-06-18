def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine maximums, minimums,
    and calculates the overall range difference between the combined set of values.

    Args:
        list_a (list): First list of numerical lengths.
        list_b (list): Second list of numerical lengths.

    Returns:
        dict: A dictionary containing 'max_combined', 'min_combined', 
              'range_difference' and a status message if lists are empty or invalid.
    
    Raises:
        ValueError: If input arguments contain non-numeric values.
    """
    # Validate inputs for numeric content
    try:
        combined = list_a + list_b
        
        max_val = float('-inf')
        min_val = float('inf')
        
        has_error = False
        
        for item in combined:
            if not isinstance(item, (int, float)):
                raise ValueError(f"Non-numeric value found: {item}")
            
            # Update maximum and minimum dynamically to handle empty lists gracefully later
            max_val = max(max_val, item)
            min_val = min(min_val, item)

        return {
            "max_combined": round(max_val), 
            "min_combined": round(min_val), 
            "range_difference": round(abs(max_val - min_val)),
            "status": f"Analysis complete for combined length count: {len(combined)}."
        }
    except ValueError as ve:
        return {"error": str(ve), "message": "Invalid input data provided.", "max_combined": None, "min_combined": None}

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user interaction or external dependencies.
    
    list_a = [10.5, 20.3, 15.7]
    list_b = [8.9, 22.4, 16.1]

    result = compare_length_lists(list_a, list_b)

    print(f"Maximum Length: {result['max_combined']}")
    print(f"Minimum Length: {result['min_combined']}")
    print(f"Range Difference: {result['range_difference']}")