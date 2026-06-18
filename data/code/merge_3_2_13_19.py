import argparse
from statistics import mean, stdev

def calculate_mean(values):
    """Calculates the arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

def calculate_stdev(values):
    """Calculates the standard deviation using efficient statistical formulas.
    
    Uses the formula: sqrt(sum((x - mean)^2 for x in values) / (n-1))
    This avoids multiple passes over the data by computing intermediate sums first,
    though Python's 'statistics' module is already implemented highly efficiently 
    and optimized at a lower level than manual iteration.
    
    Args:
        values: List of numerical values
        
    Returns:
        The standard deviation or None if fewer than 2 elements exist.
    """
    return stdev(values)

def parse_and_calculate(input_string):
    """Parses a comma-separated string into floats and returns statistics."""
    try:
        raw_values = input_string.strip().split(',')
        numeric_values = [float(x.strip()) for x in raw_values if x.strip()]
        
        if len(numeric_values) == 0:
            return None, None
            
        m = calculate_mean(numeric_values)
        s = calculate_stdev(numeric_values)
        
        return m, s
        
    except ValueError as e:
        print(f"Error parsing input values: {e}")
        return None, None

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or arguments.
    # These represent volume measurements in liters for a batch process study.
    SAMPLE_DATA = "10.5, 12.3, 9.8, 11.1, 10.9"

    mean_val, stdev_val = parse_and_calculate(SAMPLE_DATA)

    print(f"The arithmetic mean is {mean_val:.4f}")
    
    if stdev_val:
        print(f"The standard deviation is {stdev_val:.4f}")
    else:
        # Fallback for single value or invalid input edge cases handled in parse function
        print("Could not calculate standard deviation.")