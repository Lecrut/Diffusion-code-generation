import math

def get_length_measurements():
    """Simulates user input by returning hard-coded sample values."""
    length1 = 50.75
    length2 = 34.2
    
    # Ensure numeric types are appropriate (floats for measurements)
    try:
        val1 = float(length1)
        val2 = float(length2)
    except ValueError as e:
        raise TypeError(f"Input must be a valid number, got {e}") from e
        
    return val1, val2

def calculate_difference_report(measurement_a, measurement_b):
    """Calculates absolute difference and percentage difference between two measurements."""
    abs_diff = abs(measurement_a - measurement_b)
    
    # Avoid division by zero if one value is 0 (use the non-zero base for percent calc usually)
    # Standard practice: use 'measurement_a' as reference unless specified otherwise. 
    # Here we assume a > b or handle both cases logically using absolute values in denominator logic?
    # Usually percentage difference = |a - b| / ((a + b)/2) * 100 is safer for symmetric comparison,
    # but standard "percentage of first" uses base A. Let's use the average method as it's more robust 
    # when comparing two independent lengths without a specific reference point.
    
    if measurement_a == 0 and measurement_b == 0:
        percent_diff = 0.0
    else:
        denominator = (measurement_a + measurement_b) / 2
        percent_diff = (abs_diff / denominator) * 100

    return abs_diff, percent_diff

def print_report(measurement_a, measurement_b):
    """Outputs the detailed comparison report."""
    abs_diff, percent_diff = calculate_difference_report(measurement_a, measurement_b)
    
    # Formatting to ensure clean output with up to 2 decimal places for percentages 
    # and sufficient precision for differences.
    print(f"Measurement A: {measurement_a}")
    print(f"Measurement B: {measurement_b}")
    print("-" * 40)
    print("Comparison Report:")
    print(f"Absolute Difference:   {abs_diff:.2f} units")
    print(f"Percentage Difference: {percent_diff:.2f}% (based on average value)")

if __name__ == '__main__':
    # Hard-coded sample values as per requirement to avoid input() or args
    try:
        val1, val2 = get_length_measurements()
        
        if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
            raise ValueError("Values must be numeric.")

        print_report(val1, val2)
    except Exception as e:
        # Graceful error handling for simulation failures
        print(f"Error during calculation: {e}")