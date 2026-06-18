import math

def get_length_measurements():
    """Returns a tuple of two length measurements as floats."""
    return 10.5, 23.75

def calculate_absolute_difference(val1: float, val2: float) -> float:
    """Calculates the absolute difference between two values."""
    return abs(val1 - val2)

def calculate_percentage_difference(base_value: float, other_value: float) -> float:
    """Calculates the percentage difference relative to the base value.
    
    Formula: |a - b| / (0.5 * (|a| + |b|)) * 100 for symmetric comparison,
             or |a - b| / |base_value| * 100 if a specific reference is needed.
             
    This implementation uses the standard relative difference formula:
    |(val2 - val1) / ((abs(val1) + abs(val2)) / 2)| * 100 to avoid division by zero 
    and provide symmetry, unless one value is explicitly intended as a base reference.
    
    For this task's context of "percentage difference" between two measurements:
    We use the symmetric formula which is standard in scientific contexts when no specific baseline exists.
    """
    if val1 == 0 and val2 == 0:
        return 0.0
    
    # Symmetric percentage difference formula often used in physics/engineering
    denominator = (abs(val1) + abs(val2)) / 2
    if denominator == 0:
        return 0.0
        
    diff = abs(val2 - val1)
    return (diff / denominator) * 100

def generate_comparison_report(measurement_a: float, measurement_b: float):
    """Generates and prints a detailed comparison report."""
    absolute_diff = calculate_absolute_difference(measurement_a, measurement_b)
    
    # Using symmetric percentage difference for two independent measurements
    percent_diff = calculate_percentage_difference(measurement_a, measurement_b)
    
    print(f"Measurement A: {measurement_a}")
    print(f"Measurement B: {measurement_b}")
    print("-" * 40)
    print("Comparison Report:")
    print(f"Absolute Difference: {absolute_diff:.2f} units")
    print(f"Percentage Difference (Symmetric): {percent_diff:.2f}%")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts or input() calls.
    val_a, val_b = get_length_measurements()
    
    generate_comparison_report(val_a, val_b)