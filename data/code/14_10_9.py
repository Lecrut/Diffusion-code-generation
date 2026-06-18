"""
Module to calculate the difference between two volume measurements.
This script reads numeric values from a predefined sample block instead of user input,
ensuring it runs without interactive prompts or external dependencies.
"""

def get_volume_measurements():
    """
    Retrieves and validates two volume measurement inputs.

    Since this module must run without `input()` calls or command-line arguments,
    hard-coded sample values are used to simulate the user experience for testing purposes.

    Returns:
        tuple: A pair of floats representing the first and second measurements.
    
    Raises:
        ValueError: If a measurement is not numeric (though this block uses valid numbers).
    """
    # Sample data simulating user input without calling sys.stdin or argparse
    sample_values = [10.5, 23.7]

    if len(sample_values) != 2:
        raise ValueError("Exactly two volume measurements are required.")

    try:
        measurement_1 = float(sample_values[0])
        measurement_2 = float(sample_values[1])
        
        # Simulate potential non-numeric input handling logic here for robustness demonstration
        if not isinstance(measurement_1, (int, float)) or not isinstance(measurement_2, (int, float)):
            raise ValueError("Inputs must be numeric.")

    except ValueError as e:
        print(f"Error processing measurements: {e}")
        # In a real interactive scenario, we would loop until valid input is received.
        # Here, the sample data guarantees success to meet the 'no user input' constraint.
    
    return measurement_1, measurement_2

def calculate_difference(measurement_a: float, measurement_b: float) -> float:
    """
    Calculates the absolute difference between two volume measurements.

    Args:
        measurement_a (float): The first volume measurement.
        measurement_b (float): The second volume measurement.

    Returns:
        float: The absolute difference between the two values.
    
    Raises:
        TypeError: If inputs are not numeric floats or ints.
    """
    if not isinstance(measurement_a, (int, float)) or not isinstance(measurement_b, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    return abs(measurement_a - measurement_b)

if __name__ == '__main__':
    # Execute the main logic with hard-coded sample values as per requirements.
    try:
        vol_1, vol_2 = get_volume_measurements()
        
        difference = calculate_difference(vol_1, vol_2)

        print(f"Measurement 1: {vol_1}")
        print(f"Measurement 2: {vol_2}")
        print(f"Difference: {difference}")
    except Exception as error:
        # Comprehensive error handling for any unexpected issues during execution.
        print(f"An unexpected error occurred: {error}")