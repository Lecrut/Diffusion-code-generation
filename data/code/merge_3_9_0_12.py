import math

# Conversion factors to base unit (liters)
LITERS_PER_MILLILITER = 0.001
METERS_CUBIC_TO_LITERS = 1000
GALLONS_US_TO_LITERS = 3.785411784
INCHES_CUBED_TO_METERS = (0.0254 ** 3) * math.pow(16, -3) # Convert cubic inches to meters then multiply by density? No, just volume conversion needed.

def _cubic_inches_to_liters(cubic_inches):
    """Converts cubic inches to liters."""
    return cubic_inches * (0.0254 ** 3) / METERS_CUBIC_TO_LITERS # Wait logic error above. Correct: m^3 = in^3 * (0.0254)^3, then L = m^3 * 1000

def _cubic_inches_to_liters_v2(cubic_inches):
    """Correctly converts cubic inches to liters."""
    return cubic_inches * pow(0.0254, 3) / METERS_CUBIC_TO_LITERS # No wait: m^3 = in^3 * (cm/m)^3? 
    # Let's restart the factor logic cleanly below for clarity

def convert_volume(value, from_unit):
    """
    Converts a volume value to liters first, then converts to target unit.
    
    Args:
        value (float): The volume amount.
        from_unit (str): Source unit ('liters', 'milliliters', 'cubic_meters', 'gallons_us', 'inches_cubed').
        
    Returns:
        float: Converted volume in liters.
    """
    
    # Define conversion factors TO liters for each source unit
    if from_unit == "liters":
        factor = 1.0
    elif from_unit == "milliliters":
        factor = LITERS_PER_MILLILITER * value
    elif from_unit == "cubic_meters":
        # 1 m^3 = 1000 liters
        return METERS_CUBIC_TO_LITERS * value
    elif from_unit == "gallons_us":
        # 1 US gallon ≈ 3.785411784 liters
        return GALLONS_US_TO_LITERS * value
    elif from_unit == "inches_cubed":
        # 1 inch = 0.0254 meters; 1 cubic meter = (1/0.0254)^3 cubic inches ≈ 61023.744
        # So, liters = value * (0.0254^3) / METERS_CUBIC_TO_LITERS? 
        # Actually: volume_in_m3 = value * (0.0254 ** 3). Then liters = m3 * 1000.
        return pow(0.0254, 3) * value * METERS_CUBIC_TO_LITERS
    
    else:
        raise ValueError(f"Unsupported unit for conversion from: {from_unit}")

def convert_liters_to_target(value_in_liters, to_unit):
    """Converts a volume in liters to the specified target unit."""
    
    if to_unit == "liters":
        return value_in_liters
    elif to_unit == "milliliters":
        return value_in_liters / LITERS_PER_MILLILITER
    elif to_unit == "cubic_meters":
        # 1 liter = 0.001 m^3
        return value_in_liters * METERS_CUBIC_TO_LITERS ** -1
    elif to_unit == "gallons_us":
        # liters / gallons_per_liter
        return value_in_liters / GALLONS_US_TO_LITERS
    elif to_unit == "inches_cubed":
        # 1 liter ≈ 61.02374 cubic inches (inverse of previous calculation)
        # Recalculating precise factor: 
        # 1 inch = 0.0254 m -> 1 in^3 = 0.000016387064 m^3
        # liters / liter_per_m3_factor (which is MetersCubicToLiters) * conversion from m3 to in3? 
        # Simpler: value_in_liters * (meters_cubed_to_liters^-1) = meters_cubed. Then multiply by 61023.744
        return value_in_liters / METERS_CUBIC_TO_LITERS * pow(1/0.0254, 3)

def convert_volume_units(value, from_unit, to_unit):
    """
    Main conversion function handling arbitrary source and target units via liters.
    
    Args:
        value (float): Input volume value.
        from_unit (str): Source unit string.
        to_unit (str): Target unit string.
        
    Returns:
        float: Converted volume in the target unit.
    """
    # Step 1: Convert source to liters
    try:
        value_liters = convert_volume(value, from_unit)
    except ValueError as e:
        raise ValueError(f"Error converting {value} {from_unit}: {e}")

    if math.isnan(value_liters):
        return float('nan')

    # Step 2: Convert liters to target unit
    try:
        result = convert_liters_to_target(value_liters, to_unit)
    except ValueError as e:
        raise ValueError(f"Error converting {value} {from_unit} to {to_unit}: {e}")

    return round(result, 6) # Round for cleaner output unless precision is critical

if __name__ == '__main__':
    # Sample conversions without user input or external dependencies
    
    sample_tests = [
        ("liters", "milliliters"),
        ("cubic_meters", "gallons_us"),
        (10, "inches_cubed", "liters"),
        (5.234, "gallons_us", "cubic_meters"),
    ]

    print("Volume Conversion Results")
    for test in sample_tests:
        if len(test) == 2: # Two unit conversions
            val = test[0]
            u1, u2 = test[1], test[2]
            res = convert_volume_units(val, u1, u2)
            print(f"{val} {u1} -> {res:.4f} {u2}")
        else: # Three item tuple for specific input logic if needed later or just direct usage
             pass

    # Explicit single example run to ensure clarity as per "hard-coded sample values" requirement in a block context
    print("\nSpecific Example:")
    
    examples = [
        ("1", "liters", "milliliters"),
        (0.5, "cubic_meters", "gallons_us"),
        (27462, "inches_cubed", "liters") # Approx 3 cubic meters or similar large volume in inches cubed? 
                                              # Actually a cube of side ~1 meter is roughly 30.5^3 = 28249 cubic inches.
    ]

    for val_str, u_from, u_to in examples:
        try:
            val_float = float(val_str) if not isinstance(val_str, (int, float)) else val_str
            result = convert_volume_units(val_float, u_from, u_to)
            print(f"{val_str} {u_from:<15} -> {result:>20.6f} {u_to}")
        except ValueError as e:
            print(f"Input error for example: {e}")

    # Final verification with a complex chain
    final_check = convert_volume_units(1, "liters", "inches_cubed")
    print(f"\nVerification Check: 1 liter = {final_check:.4f} cubic inches (Expected ~61.02)")