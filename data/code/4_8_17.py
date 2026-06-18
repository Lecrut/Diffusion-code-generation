import math

# Mapping of distance unit abbreviations to their conversion factors relative to meters.
# Factors represent how many units in one meter, so multiplying by this factor 
# converts from that unit's value directly to meters? No: if I have 1 km = 1000 m,
# the factor for 'km' should be such that distance * factor gives meters.
# So 1 km -> multiply by 1000. 1 cm -> multiply by 0.01.
UNIT_FACTORS_TO_METERS = {
    "m": 1.0,          # meter to meter
    "km": 1_000.0,     # kilometer: 1 km = 1000 m
    "mm": 0.001,       # millimeter: 1 mm = 0.001 m
    "cm": 0.01,        # centimeter: 1 cm = 0.01 m
    "nm": 1e-9,        # nanometer: 1 nm = 1e-9 m
    "um": 1e-6,        # micrometer (micron): 1 um = 1e-6 m
    "ft": 0.3048,      # foot: 1 ft ≈ 0.3048 m
    "in": 0.0254,      # inch: 1 in = 0.0254 m
}

def normalize_distance(value, unit):
    """
    Normalize a distance measurement to meters based on the provided string abbreviation.
    
    Args:
        value (float or int): The magnitude of the distance.
        unit (str): String abbreviation representing the current unit of measure.
        
    Returns:
        float: The equivalent distance in meters.
        
    Raises:
        ValueError: If the input value is negative or if an unsupported unit string is provided.
    """
    # Handle invalid magnitude
    if not isinstance(value, (int, float)):
        raise TypeError(f"Distance value must be a number, got {type(value).__name__}")
    
    if value < 0:
        raise ValueError("Negative distance values are not supported for normalization.")

    unit = unit.strip().lower()
    
    # Check if the provided unit is recognized
    if unit not in UNIT_FACTORS_TO_METERS:
        valid_units = ", ".join(UNIT_FACTORS_TO_METERS.keys())
        raise ValueError(f"Unsupported distance unit '{unit}'. Supported units are {valid_units}.")

    factor = UNIT_FACTORS_TO_METERS[unit]
    
    # Calculate the value in meters
    return value * factor

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (5, "km"),          # 5 kilometers -> 5000 meters
        (-10, "m") if False else None, # Negative check disabled in test run logic below for clarity but kept in function
        (2540, "in"),       # 2540 inches -> 64.832 meters
        (1e-9, "nm"),       # 1 nanometer -> 1e-9 * 1 m = 1e-9 meters? Wait: 
                           # The logic is value * factor. If I have 1 nm and want meters.
                           # My function does: distance_in_meters = input_value * UNIT_FACTOR.
                           # For 'nm', factor is 1e-9 (since 1 m = 1,000,000,000 nm). 
                           # So if I have a measurement of "1" in nanometers, result is 1 * 1e-9 meters. Correct.
        (3652487.7, "ft"), # Approximate length of a football field plus some extra -> ~1109 m
    ]

    test_cases = [
        ("Test case 1: 5 km", 5, "km", 5000),
        ("Test case 2: 3.5 cm", 3.5, "cm", 0.035),
        ("Test case 3: -5 m (Error expected)", -5, "m"), # Expecting ValueError
    ]

    for test_input in samples[:4]: # Run first few valid ones to avoid complex error handling output clutter unless needed
        if len(test_input) == 2:
            val = float(test_input[0])
            unit_str = test_input[1]
            
            try:
                result_meters = normalize_distance(val, unit_str)
                print(f"{val} {unit_str.upper()} is equal to {result_meters:.6f} meters.")
                
                # Verify against expected values for sanity check within the module execution
                if test_input == (5.0, "km"):
                    assert abs(result_meters - 5000) < 1e-9, f"Expected ~5000m, got {result_meters}"
                elif test_input == (3.5, "cm"):
                    expected = 0.035
                    assert abs(result_meters - expected) < 1e-6, f"Expected {expected}m, got {result_meters}"
                    
            except Exception as e:
                print(f"Error processing input {test_input}: {type(e).__name__}: {e}")

    # Explicit test for negative value to demonstrate error handling capability in the module context.
    try:
        normalize_distance(-10, "m")
    except ValueError as ve:
        print(f"\nCorrectly caught invalid distance input (-10 m): {ve}")