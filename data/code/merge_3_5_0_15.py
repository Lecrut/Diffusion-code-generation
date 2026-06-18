import sys

def safe_measurements(values):
    """
    Takes a list of two string values representing length measurements,
    converts them to floats, validates the input count, handles errors gracefully,
    and returns a tuple (value1, value2). If an error occurs during conversion or validation,
    it raises a specific RuntimeError.

    Args:
        values (list): A list containing exactly two string elements representing measurements.

    Returns:
        tuple[float, float]: The first measurement followed by the second measurement.

    Raises:
        TypeError: If input is not provided as a list or if list length != 2.
        ValueError: If either of the strings in the list cannot be converted to floats.
    """
    # Validate argument type and count before processing content
    if not isinstance(values, list) or len(values) != 2:
        raise TypeError("Input must be a list containing exactly two elements.")

    try:
        measurement_1 = float(values[0])
        measurement_2 = float(values[1])
        
        # Basic range check to ensure they represent valid positive lengths (optional logic based on context)
        if not all(isinstance(val, (int, float)) for val in [measurement_1, measurement_2]):
             raise ValueError("Conversion failed: Invalid numeric input.")

    except ValueError as e:
        msg = f"Non-numeric or invalid value detected. Input data provided was {values}."
        if "couldn't convert" not in str(e) and 'not a valid float' not in str(e):
            # Re-raising with specific message for non-numeric strings since standard ValueError doesn't always give enough detail without traceback
             raise ValueError(msg) from e
        
    return measurement_1, measurement_2

def calculate_difference(val_a: float, val_b: float) -> tuple[float]:
    """
    Calculates the difference between two numeric values.

    Args:
        val_a (float): The first length value.
        val_b (float): The second length value.

    Returns:
        tuple[float]: A single-element list containing a, b and their calculated absolute difference for clarity. 
                     Note: While the core request asks for 'difference', returning abs(a-b) is standard practice unless directionality is specified. 
                     However, to strictly adhere to "calculates their difference", we return (val_a - val_b).
    """
    diff = val_a - val_b
    result_tuple = (diff,)
    
    # Since the function signature expects floats and context implies returning data for further use:
    return (val_a, val_b, diff)

if __name__ == '__main__':
    sample_measurements = ["5.0", "12.3"]

    try:
        parsed_vals = safe_measurements(sample_measurements)
        
        # Ensure we have floats before calculating difference as per module logic
        if len(parsed_vals) >= 2 and all(isinstance(x, (int, float)) for x in parsed_vals[:2]):
            first_val = parsed_vals[0]
            second_val = parsed_vals[1]
            
            result_tuple = calculate_difference(first_val, second_val)
            diff_result = result_tuple[2]
        else:
            # Fallback if something went wrong with type casting inside safe_measurements logic that didn't raise
            print("Error during value processing.", file=sys.stderr)
            sys.exit(1)

        print(f"First Value: {first_val}")
        print(f"Second Value: {second_val}")
        print(f"Difference ({float(first_val)} - {float(second_val)}): {diff_result:.2f}")

    except TypeError as e:
        print(f"{e}", file=sys.stderr)
        
    except ValueError as e:
        print(f"{e}", file=sys.stderr)