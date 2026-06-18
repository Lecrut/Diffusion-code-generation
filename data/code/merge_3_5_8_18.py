import math

def get_length_measurements():
    """Returns a tuple of two length measurements as floats."""
    return 10.5, 23.7

def calculate_difference(measurement_a: float, measurement_b: float) -> dict:
    """Calculates the absolute difference and percentage difference between two values.

    Args:
        measurement_a (float): First numeric length measurement.
        measurement_b (float): Second numeric length measurement.

    Returns:
        dict: A dictionary containing 'absolute_difference' and 'percentage_difference'.
    """
    abs_diff = abs(measurement_a - measurement_b)
    
    # Calculate percentage difference relative to the average of the two numbers
    if abs((measurement_a + measurement_b) / 2) == 0:
        percent_diff = 0.0
    else:
        avg_val = (measurement_a + measurement_b) / 2
        percent_diff = (abs_diff / avg_val) * 100

    return {
        "absolute_difference": round(abs_diff, 4),
        "percentage_difference": round(percent_diff, 4)
    }

def generate_report(measurement_a: float, measurement_b: float):
    """Generates and prints a detailed comparison report."""
    stats = calculate_difference(measurement_a, measurement_b)

    print(f"Measurement A: {measurement_a}")
    print(f"Measurement B: {measurement_b}")
    
    abs_diff = stats["absolute_difference"]
    pct_diff = stats["percentage_difference"]

    print("-" * 40)
    print("Comparison Report")
    print("-" * 40)
    print(f"Absolute Difference:   |{abs_diff}| units")
    print(f"Percentage Difference: {pct_diff}% relative to the average value")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input() or arguments used)
    val_a, val_b = get_length_measurements()

    generate_report(val_a, val_b)