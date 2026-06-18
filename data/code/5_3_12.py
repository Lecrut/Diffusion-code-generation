import sys

def calculate_ratio(measurement1: float, measurement2: float) -> None:
    """
    Calculates and prints the ratio of two positive length measurements.
    
    Args:
        measurement1 (float): The first length measurement.
        measurement2 (float): The second length measurement.
        
    Raises:
        ValueError: If either measurement is not a number or if it is non-positive.
    """
    try:
        # Validate that inputs are positive numbers
        if not isinstance(measurement1, (int, float)) or measurement1 <= 0:
            raise ValueError(f"First measurement must be a positive number, got {measurement1}")
        if not isinstance(measurement2, (int, float)) or measurement2 <= 0:
            raise ValueError(f"Second measurement must be a positive number, got {measurement2}")

        # Calculate and print the ratio
        result = measurement1 / measurement2
        print(result)
    except Exception as e:
        if isinstance(e, ValueError):
            raise
        else:
            # Handle unexpected errors gracefully by printing them without crashing
            sys.stderr.write(f"An error occurred: {e}\n")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access
    val1 = 10.5
    val2 = 3
    
    try:
        calculate_ratio(val1, val2)
    except ValueError as ve:
        print(f"Validation failed: {ve}", file=sys.stderr)