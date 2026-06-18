from typing import Literal, Union

def convert_length(length: float, unit_in: str) -> tuple[float, str]:
    """
    Converts a given length from one unit to another based on conversion factors relative to meters.

    Supported units (case-insensitive): 'm', 'km' (kilometers), 'cm' (centimeters), 
    'mm' (millimeters), 'ft' (feet), 'in' (inches).
    
    The function returns a tuple containing the converted length in meters and the target unit as a string.

    Args:
        length (float): The numerical value of the length to be converted. Must be non-negative.
        unit_in (str): The initial unit of measurement ('m', 'km', 'cm', 'mm', 'ft', or 'in').

    Returns:
        tuple[float, str]: A tuple where:
            - float: The equivalent length in meters.
            - str: The specified target unit string provided by the user (not automatically changed).

    Raises:
        ValueError: If the input `unit_in` is not supported or if `length` is negative.

    Examples:
        >>> convert_length(10, 'ft')
        (3.048, 'ft')  # Assuming target unit remains as provided unless modified logic requested; here we return meters internally but let's clarify the requirement based on typical usage. 
                      # Correction per standard conversion tasks usually imply converting FROM A TO B or just normalizing to a base and returning that + label?
                      # Re-reading: "returns the converted value". Usually implies changing units if different, else keeping same scale representation of meters?
                      # Let's implement full unit-to-unit conversion. If input is 'm', output should still be in 'm'. 
                      # If input is 'ft' and we don't specify target, maybe default to meters or keep original? 
                      # The prompt says "converts... from one unit to another", implying a change unless same.
                      # However, without explicit second argument for `unit_out`, the standard interpretation in such single-arg converters (besides input length and source) is often:
                      # 1. Normalize everything to meters internally? 
                      # But then what does 'returns' mean regarding unit label?
                      # Let's assume the function converts FROM the given UNIT TO METERS, as that is a safe default base conversion unless specified otherwise.
                      
        >>> convert_length(500, 'cm') -> (5.0, 'm')  <-- Converting to meters and returning value in meters? 
        Or maybe it just returns the number scaled correctly if we treat "unit type" as an instruction for scale?
        
    Clarification Strategy: Since no `target_unit` argument is requested, I will implement conversion FROM any supported unit TO METERS. The returned tuple will be (value_in_meters, 'm'). 
    This satisfies "optimized function... returns the converted value".

    """
    
    # Define conversion factors relative to meters
    units_map: dict[str, float] = {
        'm': 1.0,
        'km': 1e3,      # multiply by km factor then divide? No. 
                        # To convert X km -> m, we do X * 1000. So if stored as factor for meters: 1 km = 1000 m. Factor is 1/1000 of a meter?
                        # Let's store the value in that unit equivalent to how many Meters. 
        'cm': 1e-2,     # 1 cm = 0.01 meters -> wait, if I have X CMs, result_in_mers = X * 0.01. So factor is 0.01 relative to meter count?
                        # Actually easier: convert_to_base(factor) where base=meters. 
                        # km: 1 unit = 1000 meters -> multiply by 1000. Factor = 1e3.
        'mm': 1e-3,     # Wait logic above was flipped in head? Let's be precise.
        
    }

    # Redefining map clearly: factor * input_length gives length in Meters.
    base_conversion_factors: dict[str, float] = {
        'm': 1.0,       # m -> m: x1
        'km': 1e3,      # km -> m: x1000 (since 1 km = 1000 meters) -- Wait. If input is "5", meaning 5 kilometers? Yes. 
                        # So result_meters = 5 * 1000 = 5000m. Correct.
        'cm': 1e-2,     # cm -> m: x0.01 (since 1 cm = 0.01 meters). Input "5" means 5cm? Result 0.05m. Correct.
                        # Wait previous line said km factor was 1e3. 
                        # Let's check cm again. If I have length in cm, to get meters: Length_cm * (1 meter / 100 cm) = Length_cm * 0.01. So factor is 0.01 or 1e-2? Yes.
        'mm': 1e-3,     # mm -> m: x0.001. 
                        # What about feet and inches?
        'ft': 0.3048,   # ft -> m: multiply by 0.3048 (standard)
        'in': 0.0254,   # in -> m: multiply by 0.0254
    
    }

    unit_lower = unit_in.lower() if isinstance(unit_in, str) else ""

    if not base_conversion_factors.get(unit_lower):
        raise ValueError(f"Unsupported input unit: {unit_in}. Supported units are 'm', 'km', 'cm', 'mm', 'ft', 'in'.")

    # Validate non-negative length
    if length < 0:
        raise ValueError("Length must be a non-negative number.")

    meters = base_conversion_factors[unit_lower] * length
    
    return (float(meters), "m")

if __name__ == '__main__':
    sample_tests = [
        ("1", "ft"),      # 1 ft -> m
        ("50.8", "in"),   # ~2 yards? Just standard conversion check. 
                        # Actually let's pick nice numbers: 39 inches is roughly a yard (but not exactly). Let's just use floats or ints as input type hint says float.
        ("10", 'km'),     # 10 km -> m
        ("254", "mm"),    # Exact to 1 meter? No, 254 mm = 25.4 cm != 1m. 
                        # Wait 1000 mm = 1m. So input '1' with unit 'km'? No.
                        # Let's use simple ones: 39 inches isn't nice. 
                        # How about converting feet to meters? 2 ft -> ~60cm (0.6096).
        ("5", "ft"),      # Common conversion example
        
    ]

    for length_str, unit in sample_tests:
        try:
            val_in_meters = convert_length(float(length_str), unit)
            print(f"Converting {length_str} {unit}:")
            result_val, result_unit = val_in_meters[0], val_in_meters[1] # Wait return is tuple (val, 'm') always? 
            # My implementation returns ('value', "m"). This matches the logic derived.
            print(f"  Result: {result_val} meters")
        except Exception as e:
            print(f"Error for input ({length_str}, {unit}): {e}")

    # Additional explicit test case from prompt requirements implicitly (hard coded sample values)
    # Testing mixed types logic if needed, but type hint says float.
    
    specific_check = convert_length(10.5, 'm') 
    print(f"Specific check: 10.5 m -> {specific_check}")