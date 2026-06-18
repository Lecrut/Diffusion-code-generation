def convert_length(length: float, unit_str: str) -> dict[str, float]:
    """
    Converts a numerical length from one supported unit to meters 
    and optionally back to other units if needed based on input context logic.
    
    Since the task requires returning conversions for 'meters', 'feet', 'kilometers'
    given an *input* target unit, this function interprets the request as:
    "Convert length into all three supported units."

    Args:
        length (float): The numerical value of the length.
        unit_str (str): A string representing a valid input unit ('meters', 'feet', or 'kilometers').

    Returns:
        dict[str, float]: Dictionary containing the converted values for all three units 
                         with keys 'meters', 'feet', and 'kilometers'.

    Raises:
        ValueError: If the provided unit_str is not one of the supported units.
    """
    valid_units = {'meters': 1.0, 'feet': 3.28084, 'kilometers': 1e-3}
    
    if unit_str not in valid_units:
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are meters, feet, kilometers.")

    # Base conversion factor to meters (for reference)
    # However, the prompt implies we start with a 'numerical length' and a 'target unit string'.
    # A common interpretation of "converts ... to a predefined set" given an input is 
    # that the input defines the scale or type. But strictly reading:
    # "takes a numerical length AND a target unit string, and performs the necessary conversion".
    
    # Let's assume the standard behavior for such tools: The user provides a value in ONE specific unit,
    # but wants to see it expressed across ALL supported units? 
    # OR does 'target unit' mean convert TO that specific one only?
    
    # Re-reading carefully: "performs the necessary conversion". Singular.
    # It likely means: Convert the given `length` (implicitly in meters or generic float?) 
    # INTO the specified `unit_str`. 
    # BUT, usually these tasks imply the input length is unitless relative to meters unless stated otherwise?
    # Or perhaps the user provides a value IN THE TARGET UNIT and wants it normalized?
    
    # Let's adopt the most robust functional interpretation:
    # The function takes a number `length` which represents magnitude. 
    # If no explicit source unit is given, we assume the input `length` corresponds to the `unit_str`.
    # We then convert that value into Meters (base), Feet, and Kilometers?
    
    # Wait, "takes ... length AND target unit string".
    # Scenario A: Input = 10 feet. Target = meters. Output = 32.8...
    # Since only ONE target is requested per call based on the prompt structure ("a target unit"), 
    # but the docstring example logic above suggested all three, let's stick to the strictest reading:
    # Convert `length` (assumed to be in meters for simplicity unless specified otherwise) TO `unit_str`.
    
    # Actually, looking at standard conversion tasks: Usually you provide Value + SourceUnit -> TargetValue.
    # Here we have Length and Target Unit. The source unit is missing. 
    # Assumption: The input length is a magnitude in METERS (SI base). We convert it TO the target string.
    
    if unit_str == 'meters':
        return {'meters': float(length), 'feet': 0.0, 'kilometers': 0.0}

    elif unit_str == 'feet':
        # Convert meters to feet: length * 3.28084
        converted_feet = round(length * 3.28084)
        return {'meters': float(length), 'feet': converted_feet, 'kilometers': 0.0}

    elif unit_str == 'kilometers':
        # Convert meters to kilometers: length / 1000
        converted_km = round(length * 1e-3)
        return {'meters': float(length), 'feet': 0.0, 'kilometers': converted_km}

    else:
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are meters, feet, kilometers.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Case 1: Convert 500 (meters) to feet
    result_m_to_ft = convert_length(500.0, 'feet')
    
    # Case 2: Convert 1584 (feet) back to meters? 
    # Note: If input is assumed meters-based, then 1584 implies 1584 meters -> feet would be huge.
    # To make the sample meaningful for a user who might think "I have this amount in X", we assume the function
    # normalizes everything to Meters internally first (treating input as SI base) OR 
    # treats input as Value IN THE TARGET UNIT? 
    
    # Let's refine the logic based on typical usage: User says "Convert 10 feet". Function returns meters.
    # Since we don't have source unit, let's assume Input Length is ALWAYS in METERS by default unless specified otherwise? 
    # No, that makes 'feet' target useless if input isn't defined as such.
    
    # Alternative Interpretation (More likely for a "purely functional" converter):
    # The function converts the magnitude `length` from an implicit base unit to the `unit_str`.
    # Let's assume the implicit source is METERS. 
    # Example: User has 10 meters, wants feet -> convert_length(10, 'feet') => returns value in feet (32.8).
    
    print("Sample Output for converting 500 Meters to Feet:")
    print(result_m_to_ft)

    print("\n---\n")
    
    # Case 3: Convert 1640 meters to kilometers
    result_m_to_km = convert_length(1.64, 'kilometers')
    print("Sample Output for converting 1.64 Meters to Kilometers:")
    print(result_m_to_km)

    try:
        # Case 4: Error handling example
        invalid_result = convert_length(500, 'yards')
    except ValueError as e:
        print(f"\nCaught expected error for unsupported unit 'yards': {e}")