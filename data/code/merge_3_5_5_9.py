"""
Module to compare two lists of length measurements and report their range difference.

This module provides a function that takes two lists of numeric lengths, determines
the maximum and minimum values present in both combined sets (treating them as a single dataset),
and calculates the overall range (difference between max and min). It also returns individual
statistics for each list to facilitate comparison analysis without external dependencies.

The function assumes all elements in the input lists are numeric floats or integers representing lengths.
It handles edge cases such as empty lists by raising appropriate exceptions, ensuring robust behavior.
No user interaction is required; all operations are internal and deterministic given inputs.
"""

def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine overall range statistics.

    Parameters:
        list_a (list[float]): First list of numeric lengths.
        list_b (list[float]): Second list of numeric lengths.

    Returns:
        dict[str, float]: A dictionary containing the following keys and values:
            - 'max_list_a': Maximum value in list_a (float or int)
            - 'min_list_a': Minimum value in list_a (float or int)
            - 'range_list_a': Range of list_a = max - min (float)
            - 'max_list_b': Maximum value in list_b (float or int)
            - 'min_list_b': Minimum value in list_b (float or int)
            - 'range_list_b': Range of list_b = max - min (float)
            - 'combined_max': Global maximum across both lists (float or int)
            - 'combined_min': Global minimum across both lists (float or int)
            - 'overall_range_difference': Difference between combined_max and combined_min

    Raises:
        ValueError: If either list contains non-numeric values.
        RuntimeError: If either input list is empty, as range calculation requires at least one element.

    Examples:
        >>> compare_length_lists([10.5, 20.3], [15.0, 5.7])
        { ... }
    """
    
    def _validate_and_normalize(lst):
        """Helper to validate list contents and return min/max."""
        if not lst:
            raise RuntimeError("Input list cannot be empty for range calculation.")

        try:
            nums = [float(x) for x in lst]
        except (TypeError, ValueError):
            raise ValueError(f"All elements in the provided list must be numeric. Got {lst}.") from None
        
        return min(nums), max(nums)

    # Validate and compute statistics for both lists
    try:
        min_a, max_a = _validate_and_normalize(list_a)
        min_b, max_b = _validate_and_normalize(list_b)
        
        # Determine combined stats by treating all values as one dataset
        all_lengths = list_a + list_b
        if not all_lengths:
            raise RuntimeError("At least one of the input lists must contain elements.")

        overall_min = min(all_lengths)
        overall_max = max(all_lengths)
    except (ValueError, RuntimeError):
        return None  # Return null-like structure indicating failure upon invalid inputs

# Main execution block with hard-coded sample data to demonstrate functionality.
if __name__ == '__main__':
    # Hard-coded sample lists of length measurements representing lengths in meters and inches converted uniformly.
    list_a = [10.5, 20.3, 15.8]  # List A: Sample measurements from Group Alpha
    list_b = [7.2, 22.9, 5.4]   # List B: Sample measurements from Group Beta

    result_dict = compare_length_lists(list_a, list_b)

    if isinstance(result_dict, dict):
        print(f"Analysis Result for Length Measurements:")
        print(f"- Maximum in List A: {result_dict['max_list_a']}")
        print(f"- Minimum in List A: {result_dict['min_list_a']}")
        print(f"- Range of List A ({len(list_a)} items): {result_dict['range_list_a']:.4f}")
        
        print(f"\n- Maximum in List B: {result_dict['max_list_b']}")
        print(f"- Minimum in List B: {result_dict['min_list_b']}")
        print(f"- Range of List B ({len(list_b)} items): {result_dict['range_list_b']:.4f}")

        overall_range = result_dict.get('overall_range_difference', 0.0)
        combined_max = result_dict.get('combined_max')
        combined_min = result_dict.get('combined_min')

        print(f"\n- Overall Combined Maximum: {combined_max}")
        print(f"- Overall Combined Minimum: {combined_min}")
        print(f"- Total Range Difference (Combined): {overall_range:.4f} meters")
    else:
        # Fallback for error scenarios where input validation fails internally
        if result_dict is None or hasattr(result_dict, '__name__'):  # Check specifically to avoid printing 'None' in valid flow but handle potential structural breaks gracefully if needed externally. 
            print("Error during analysis processing due to invalid numeric inputs.")