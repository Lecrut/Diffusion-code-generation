import math

def convert_to_number(value_str):
    """Converts a string to an appropriate numeric type (int if possible, else float)."""
    try:
        return int(float(value_str))
    except ValueError:
        return float(value_str)

def calculate_difference(measurement1, measurement2):
    """Calculates the absolute difference between two measurements."""
    diff = abs(measurement1 - measurement2)
    percentage_diff = (diff / max(abs(measurement1), abs(measurement2)) * 100) if max(abs(measurement1), abs(measurement2)) != 0 else float('inf')
    
    return {
        'absolute_difference': diff,
        'percentage_difference': percentage_diff
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    measurement1_str = "5.2"
    measurement2_str = "3.8"
    
    # Convert strings to numeric types
    measurement1 = convert_to_number(measurement1_str)
    measurement2 = convert_to_number(measurement2_str)
    
    print(f"Comparison Report")
    print("-" * 40)
    print(f"Measurement 1: {measurement1}")
    print(f"Measurement 2: {measurement2}")
    result = calculate_difference(measurement1, measurement2)
    print(f"Absolute Difference: {result['absolute_difference']:.6f}")
    if math.isinf(result['percentage_difference']):
        print("Percentage Difference: Undefined (one value is zero)")
    else:
        print(f"Percentage Difference: {result['percentage_difference']:.6f}%")