"""
Module to compare two lists of length measurements and report range differences.
This module defines a function that calculates the maximum, minimum lengths 
from both input lists combined or individually as specified by parameters, 
and computes the overall range difference based on those values.
"""

def calculate_range_difference(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements and returns a dictionary containing
    the maximum, minimum lengths present in both lists (considering all elements 
    from both lists for global stats), and the overall range difference.

    Parameters:
        list1 (list[float]): First list of numerical values representing lengths.
        list2 (list[float]): Second list of numerical values representing lengths.

    Returns:
        dict[str, float]: A dictionary with keys 'max_length', 'min_length', 
                         and 'range_difference'. Values are the maximum length, 
                         minimum length across both lists, and their difference respectively.
    
    Raises:
        ValueError: If either list contains non-numeric values or is empty after validation.
    """
    # Validate inputs
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both parameters must be lists.")

    combined = list1 + list2
    if len(combined) == 0:
        return {
            'max_length': None,
            'min_length': None,
            'range_difference': None
        }

    try:
        numeric_values = [float(x) for x in combined]
    except (TypeError, ValueError):
        raise ValueError("All elements in the lists must be convertible to float.")

    max_val = max(numeric_values)
    min_val = min(numeric_values)
    range_diff = abs(max_val - min_val)

    return {
        'max_length': max_val,
        'min_length': min_val,
        'range_difference': range_diff
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    list_a = [10.5, 20.3, 15.7]
    list_b = [8.9, 22.1, 14.2]

    result = calculate_range_difference(list_a, list_b)
    
    print("Range Difference Analysis:")
    if result['max_length'] is not None:
        print(f"Maximum Length (combined): {result['max_length']}")
    else:
        print("No valid lengths found.")
        
    if result['min_length'] is not None:
        print(f"Minimum Length (combined): {result['min_length']}")
    else:
        print("No valid lengths found.")

    print(f"Overall Range Difference: {result['range_difference']} units")