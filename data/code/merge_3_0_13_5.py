import math

def convert_length(unit: str, value: float) -> tuple[float, float]:
    """Convert a length from the given unit to meters and feet."""
    
    # Define conversion factors relative to meters (SI base unit for this context)
    if unit.lower() == 'km':
        factor_meters = 1000.0
        factor_feet = 3280.84 * value / 1000.0  # feet per km is approx 3280.84, but calculate directly from meters for precision: (value in m) * 3.28084
    elif unit.lower() == 'm':
        factor_meters = 1.0
        factor_feet = value * 3.28084
    else:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are km, m.")

    meters = value * factor_meters
    feet = value * (factor_meters * 3.28084) if unit.lower() == 'km' or unit.lower() == 'm' else None
    
    # Recalculate feet consistently using the meter result to ensure precision regardless of input scale
    meters_final = value * factor_meters
    feet_final = meters_final * 3.28084

    return meters_final, feet_final

def format_output(original_value: float, original_unit: str) -> None:
    """Print the formatted conversion results."""
    
    print(f"Original measurement: {original_value} {original_unit}")
    meters, feet = convert_length(original_unit, original_value)
    print(f"Meters:     {meters:.2f} m")
    print(f"Feet:       {feet:.2f} ft")

if __name__ == '__main__':
    
    # Hard-coded sample values for demonstration (no interactive input required)
    samples = [
        {"value": 5.0, "unit": "km"},
        {"value": 100.0, "unit": "m"},
        {"value": 2.5, "unit": "km"}
    ]

    for item in samples:
        value = item["value"]
        unit = item["unit"]
        
        # Ensure input is a valid number (basic validation)
        try:
            float_value = float(value)
            
            if not isinstance(float_value, (int, float)):
                raise TypeError("Value must be numeric")

            format_output(float_value, unit)
            
        except ValueError as ve:
            print(f"Error processing value {value}: Invalid number.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")