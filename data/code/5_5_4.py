def compare_length_lists(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine the maximum 
    and minimum lengths present in both lists combined. Returns a dictionary
    containing these values along with their range difference.

    Parameters:
        list1 (list[float]): First list of length measurements.
        list2 (list[float]): Second list of length measurements.

    Returns:
        dict[str, float]: A dictionary with keys 'overall_max', 
                         'overall_min', and 'range_difference'.
    
    Raises:
        ValueError: If either input is not a list or contains non-numeric values.
    """
    if not isinstance(list1, list) or not all(isinstance(x, (int, float)) for x in list1):
        raise TypeError("Input must be a list of numeric values.")
    if not isinstance(list2, list) or not all(isinstance(x, (int, float)) for x in list2):
        raise TypeError("Input must be a list of numeric values.")

    combined = list1 + list2
    overall_min = min(combined)
    overall_max = max(combined)
    range_difference = overall_max - overall_min

    return {
        'overall_max': float(overall_max),
        'overall_min': float(overall_min),
        'range_difference': float(range_difference)
    }

if __name__ == '__main__':
    # Sample data without user input or external dependencies
    sample_list1 = [5.2, 8.7, 3.4, 6.9]
    sample_list2 = [4.0, 9.1, 2.3, 7.5]

    result = compare_length_lists(sample_list1, sample_list2)

    print("Comparison Results:")
    print(f"Overall Maximum Length: {result['overall_max']}")
    print(f"Overall Minimum Length: {result['overall_min']}")
    print(f"Range Difference: {result['range_difference']}")