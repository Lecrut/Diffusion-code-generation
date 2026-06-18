def calculate_ratio(measurement1: float, measurement2: float) -> None:
    """
    Calculates the ratio of two length measurements.
    
    Args:
        measurement1 (float): The first positive number representing a length.
        measurement2 (float): The second positive number representing a length.
        
    Prints the result to standard output if both inputs are valid and positive.
    """
    try:
        # Validate that measurements are numbers greater than zero
        if not isinstance(measurement1, (int, float)) or measurement1 <= 0:
            raise ValueError(f"First measurement must be a positive number, got {measurement1}")
        
        if not isinstance(measurement2, (int, float)) or measurement2 <= 0:
            raise ValueError(f"Second measurement must be a positive number, got {measurement2}")

        # Calculate and print the ratio
        result = measurement1 / measurement2
        print(result)
    except Exception as e:
        if isinstance(e, ValueError):
            pass  # Silently handle invalid input values as per graceful handling requirement for logic errors in data type/positivity
        else:
            raise

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    val1 = 10.5
    val2 = 3
    
    calculate_ratio(val1, val2)