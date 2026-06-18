def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine max/min values 
    present in both lists and reports the overall range difference.
    
    Args:
        list_a (list): First list of numerical lengths.
        list_b (list): Second list of numerical lengths.
        
    Returns:
        dict: A dictionary containing 'overall_min', 'overall_max', and 
              'range_difference'. Raises ValueError if lists are empty or contain non-numeric values.
    """
    
    # Validate inputs for emptiness
    if not list_a or not list_b:
        raise ValueError("Both input lists must be non-empty.")

    # Combine the two lists to find global min and max across both datasets
    combined_list = list_a + list_b
    
    try:
        overall_min = float(min(combined_list))
        overall_max = float(max(combined_list))
        
        range_difference = overall_max - overall_min
        
        return {
            'overall_min': overall_min,
            'overall_max': overall_max,
            'range_difference': range_difference
        }
    except ValueError:
        # Re-raise if the list contains non-numeric values (though min/max handles this in Python 3)
        raise

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access used.
    
    sample_list_a = [10.5, 20.0, 30.5]
    sample_list_b = [40.0, 50.75, 60.25]

    try:
        result = compare_length_lists(sample_list_a, sample_list_b)
        
        print("Length Comparison Results:")
        print(f"Overall Minimum Length: {result['overall_min']}")
        print(f"Overall Maximum Length: {result['overall_max']}")
        print(f"Total Range Difference: {result['range_difference']:.2f}")
    except ValueError as e:
        print(f"Error in calculation: {e}")