"""
Volume Unit Converter Module

This script demonstrates the conversion between common volume units:
- Liters (L)
- Milliliters (mL)
- Cubic meters (m³)
- Gallons (US liquid gallons, gal)

Conversion factors are defined relative to one base unit or directly 
between pairs where applicable. The implementation uses standard SI and US customary conversions.

Note: This module does not use any interactive input functions like input() or sys.stdin.read().
It operates entirely on hard-coded sample values within the main execution block.
"""

# Define conversion factors relative to 1 Liter (L) as the base unit for simplicity,
# though we can also derive them directly from each other if needed.
# Factors are stored such that: result = value * factor_to_base

CONVERSION_TO_LITERS = {
    "liters": 1.0,           # 1 L -> 1 L
    "milliliters": 0.001,   # 1 mL -> 0.001 L
    "cubic_meters": 0.001,  # 1 m³ = 1000 L => factor is 1/1000 relative to base? 
                            # Wait, let's redefine the dictionary logic clearly below in code.
}

# Let's use a more robust approach: define factors to convert FROM that unit TO Liters.
FACTORS_TO_LITERS = {
    "liters": 1.0,           # To get liters from liters, multiply by 1
    "milliliters": 0.001,   # To get liters from milliliters (e.g., 500 mL * 0.001)
    "cubic_meters": 1000,   # To get liters from cubic meters (1 m³ = 1000 L)
    "gallons": 3.785411784, # To get liters from US gallons (1 gal ≈ 3.785... L)
}

# Define factors to convert FROM Liters TO the target unit for easier output formatting if desired,
# or we can just invert FACTORS_TO_LITERS and round appropriately.
FACTORS_FROM_LITERS = {unit: 1 / factor for unit, factor in FACTORS_TO_LITERS.items()}

def convert_volume(value: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
    """
    Converts a volume value between different units.

    Args:
        value (float): The numeric value of the volume.
        from_unit (str): Source unit string ('liters', 'milliliters', 'cubic_meters', 'gallons').
        to_unit (str): Target unit string ('liters', 'milliliters', 'cubic_meters', 'gallons').

    Returns:
        tuple[float, dict]: 
            - The converted value as a float.
            - A dictionary containing the original input and output details for logging/debugging.

    Raises:
        ValueError: If an unsupported unit is provided.
    
    Logic:
        1. Convert 'from_unit' to Liters using FACTORS_TO_LITERS.
        2. Convert Liters to 'to_unit' using the inverse of FACTORS_TO_LITERS (which are stored in FACTORS_FROM_LITERS).
           Alternatively, calculate directly: value_in_target = value_source * factor_from_to.
    """
    
    # Validate units against supported set
    valid_units = {"liters", "milliliters", "cubic_meters", "gallons"}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Unsupported unit '{from_unit}' (source) or '{to_unit}' (target). Valid units: {valid_units}")

    # Step 1: Convert source value to Liters
    liters_value = value * FACTORS_TO_LITERS[from_unit]

    # Step 2: Convert Liters to target unit
    final_value = liters_value / FACTORS_TO_LITERS[to_unit]

    return final_value, {
        "input": {"value": value, "unit": from_unit},
        "output": {"value": round(final_value, 6), "unit": to_unit}
    }

def format_output(value: float, unit: str) -> str:
    """Formats the numeric result into a readable string."""
    if isinstance(unit, dict):
        # Handle case where output is already formatted in convert_volume return (though here we expect just value/unit or similar logic)
        pass
    
    # Assuming 'value' and 'unit' are passed as separate arguments for flexibility
    unit_name = str(unit).lower()

    if abs(value) < 0.01:
        precision = "f6"
    else:
        precision = "g2" 

    return f"{format(value, precision)} {unit_name}"

if __name__ == '__main__':
    
    # Hard-coded sample values and conversion scenarios to demonstrate functionality without user input.
    SAMPLE_DATA = [
        {"value": 10, "from_unit": "liters", "to_unit": "milliliters"},
        {"value": 5, "from_unit": "cubic_meters", "to_unit": "gallons"},
        {"value": 7.5, "from_unit": "gallons", "to_unit": "liter"}, # Note: 'liters' is accepted but input spec says case insensitive usually? 
                                                                   # Let's stick to exact keys defined in FACTORS_TO_LITERS for strictness or normalize them here.
        {"value": 20, "from_unit": "milliliters", "to_unit": "cubic_meters"},
    ]

    print("=" * 60)
    print("Volume Unit Converter Demo")
    print("=" * 60)

    for item in SAMPLE_DATA:
        val = item["value"]
        from_u = item["from_unit"]
        to_u = item["to_unit"].lower() # Normalize case
        
        try:
            result_val, details = convert_volume(val, from_u, to_u)
            
            print(f"\nConversion Scenario:")
            input_str = f"{val} {from_u}"
            output_str = format_output(result_val, str(to_u))
            
            print("-" * 40)
            print("Input:    ", input_str)
            print("Output:   ", output_str)
            print(f"\nDetails:")
            for k, v in details.items():
                if isinstance(v, dict):
                    print(f"  {k}:")
                    # Flatten nested dicts slightly for readability or just iterate keys
                    pass
            
        except ValueError as e:
            print(f"Error processing scenario with value {val} from {from_u} to {to_u}: {e}")

    print("\n" + "=" * 60)
    print("Demo completed successfully.")