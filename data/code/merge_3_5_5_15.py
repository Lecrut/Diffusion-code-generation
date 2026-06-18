import math

def compare_length_lists(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine the maximum and minimum 
    lengths present in both lists combined, then calculates the overall range difference.
    
    Args:
        list1 (list[float]): First list of length measurements.
        list2 (list[float]): Second list of length measurements.
        
    Returns:
        dict[str, float]: A dictionary containing 'max_length', 'min_length', and 'range_difference'.
    """
    if not list1 or not list2:
        raise ValueError("Both lists must contain at least one element.")

    combined = list1 + list2
    
    max_len = max(combined)
    min_len = min(combined)
    
    range_diff = abs(max_len - min_len)
    
    return {
        "max_length": float(max_len),
        "min_length": float(min_len),
        "range_difference": float(range_diff)
    }

if __name__ == '__main__':
    sample_list1 = [5.2, 7.8, 3.4]
    sample_list2 = [6.0, 9.1, 4.5]
    
    result = compare_length_lists(sample_list1, sample_list2)
    print(f"Max Length: {result['max_length']}")
    print(f"Min Length: {result['min_length']}")
    print(f"Range Difference: {result['range_difference']}")