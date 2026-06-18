import math

def compare_length_lists(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine maximum and minimum lengths 
    present in both lists and reports the overall range difference.
    
    Args:
        list1 (list[float]): First list of numerical values representing lengths.
        list2 (list[float]): Second list of numerical values representing lengths.
        
    Returns:
        dict[str, float]: A dictionary containing 'max_length', 'min_length', and 
                         'range_difference'. If either input is empty or contains non-numeric 
                         data, appropriate error handling could be added here if needed, 
                         but this implementation assumes valid numeric inputs as per task constraints.
    """
    # Combine both lists to find global max and min across all measurements
    combined = list1 + list2
    
    if not combined:
        return {
            'max_length': 0.0,
            'min_length': float('inf'),
            'range_difference': 0.0
        }

    # Calculate maximum length present in both lists (combined)
    max_length = max(combined)
    
    # Calculate minimum length present in both lists (combined)
    min_length = min(combined)
    
    # Ensure we don't divide by zero or get infinity issues for range calculation
    if math.isinf(min_length):
        return {
            'max_length': float('nan'),
            'min_length': float('nan'),
            'range_difference': 0.0
        }

    # Calculate the overall range difference (difference between max and min)
    range_difference = abs(max_length - min_length) if not math.isnan(range_difference := max_length - min_length) else 0.0
    
    return {
        'max_length': max_length,
        'min_length': min_length,
        'range_difference': range_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    list_a = [10.5, 23.7, 45.2]
    list_b = [67.8, 90.1, -5.3]

    result = compare_length_lists(list_a, list_b)

    print("Length Comparison Results:")
    print(f"Maximum Length: {result['max_length']}")
    print(f"Minimum Length: {result['min_length']}")
    print(f"Overall Range Difference: {result['range_difference']:.2f}")