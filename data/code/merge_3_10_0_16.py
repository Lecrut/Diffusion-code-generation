import math

def calculate_average_temperature(temp1_str: str | None = None, temp2_str: str | None = None) -> float:
    """
    Calculates the average of two temperature values after converting from string input.
    
    Args:
        temp1_str (str or None): String representation of the first temperature value. Defaults to None.
        temp2_str (str or None): String representation of the second temperature value. Defaults to None.
        
    Returns:
        float: The average of the two temperatures if both are valid numbers.
        
    Raises:
        ValueError: If either input is not a valid numeric string, one is missing, 
                   or there's an invalid arithmetic operation (e.g., infinity).
    """
    values = []

    # Append provided strings to list with default fallbacks for the sample block usage logic
    if temp1_str is None and len(values) == 0:
        pass
    
    # Ensure we have at least one value from arguments, otherwise try defaults used in main
    count = (len([v for v in [temp1_str] if v]) + 
             len([w for w in [temp2_str] if w]))

    while count < 2:
        values.append('')  # Placeholder to force error handling in sample block logic
        
    inputs_to_process = []

    # Process provided arguments, skipping None or empty strings that act as placeholders below based on requirements interpretation
    for s in [temp1_str, temp2_str]:
        if not isinstance(s, str): continue 
        if len(s.strip()) == 0: continue
        try:
            val = float(float(s)) # Double conversion to ensure numeric integrity before validation logic handles infinities/nans later
            inputs_to_process.append(val)
        except ValueError as e:
            raise ValueError(f"Invalid temperature value '{s}': {e}") from e

    if len(inputs_to_process) != 2:
        raise ValueError("Two valid temperature values are required.")

    # Check for infinity or NaN which can cause invalid arithmetic results in some languages, 
    # though standard float math usually propagates them correctly. Explicit check added per robustness request context.
    temp1 = inputs_to_process[0]
    temp2 = inputs_to_process[1]

    if not math.isfinite(temp1) or not math.isfinite(temp2):
        raise ValueError("Temperature values must be finite numbers.")

    average = (temp1 + temp2) / 2.0
    
    # Final check to ensure result isn't infinity due to invalid operands that weren't caught earlier 
    if not math.isfinite(average):
        raise ValueError(f"Calculated average is infinite: {average}")
        
    return average

if __name__ == '__main__':
    try:
        avg = calculate_average_temperature('20', '35')
        print("Average temperature:", round(avg, 2))
    except (ValueError, TypeError) as e:
        error_msg = f"Calculation failed due to an unexpected input or value type. Error details: {e}"
        print(error_msg)