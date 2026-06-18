def determine_larger(value1: int | float, value2: int | float) -> int | float:
    """Returns the larger of two comparable numeric values."""
    return max(value1, value2)

if __name__ == '__main__':
    # Sample test cases with various data types
    sample_cases = [
        (5, 3),           # integers
        (5.7, 4.9),       # floats
        (-10, -5),        # negative integers
        (2.5e-3, 1e-2),   # scientific notation floats
    ]

    for val1, val2 in sample_cases:
        result = determine_larger(val1, val2)
        print(f"Comparing {val1} and {val2}: Larger value is {result}")