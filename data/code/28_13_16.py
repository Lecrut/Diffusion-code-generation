def determine_larger(value1: int | float, value2: int | float) -> int | float:
    """
    Returns the larger of two comparable numeric values (int or float).
    
    Args:
        value1 (int | float): The first number to compare.
        value2 (int | float): The second number to compare.
        
    Returns:
        int | float: The larger of the two input values.
    """
    return max(value1, value2)

if __name__ == '__main__':
    # Sample test cases with hardcoded values
    sample_cases = [
        (3, 5),           # integers -> should return 5
        (-10.5, -2.4),   # floats -> should return -2.4
        (0, 0),          # equal -> returns the value itself
        (99, 876),       # large positive ints -> should return 876
        (3.14, 2.71)     # pi-like floats -> should return 3.14
    ]

    for val1, val2 in sample_cases:
        result = determine_larger(val1, val2)
        print(f"Larger of {val1} and {val2} is {result}")