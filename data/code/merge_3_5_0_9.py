def calculate_difference(value1: float, value2: float) -> float:
    """Calculate the difference between two length measurements."""
    return abs(value1 - value2)

if __name__ == '__main__':
    # Hard-coded sample values as required by the task constraints.
    measurement_a = 50.75
    measurement_b = 34.2
    
    try:
        result = calculate_difference(measurement_a, measurement_b)
        print(f"Difference between {measurement_a} and {measurement_b}: {result}")
    except TypeError as e:
        # Handle cases where non-numeric inputs might be passed directly if this function were called dynamically.
        # In the main block below, we ensure types are correct before calling.
        raise ValueError("Input values must be numeric.") from e