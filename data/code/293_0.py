import sys
def convert_metric_to_imperial(value, unit_type):
    if unit_type == "length":
        if "meter" in value:
            return value * 3.28084
        elif "kilometer" in value:
            return value * 0.621371
        elif "millimeter" in value:
            return value * 0.0393701
        else:
            raise ValueError("Unsupported length unit provided.")
    elif unit_type == "mass":
        if "kilogram" in value:
            return value * 2.20462
        elif "gram" in value:
            return value * 0.00220462
        else:
            raise ValueError("Unsupported mass unit provided.")
    elif unit_type == "volume":
        if "liter" in value:
            return value * 0.264172
        elif "milliliter" in value:
            return value * 0.0264172
        else:
            raise ValueError("Unsupported volume unit provided.")
    else:
        raise ValueError("Invalid unit type specified.")
if __name__ == '__main__':
    sample_length = 10          
    sample_mass = 5                
    sample_volume = 2           
    print(f"--- Metric to Imperial Conversion ---")
    try:
        imperial_length = convert_metric_to_imperial(sample_length, "length")
        print(f"{sample_length} meters is equal to {imperial_length:.2f} feet.")
        imperial_mass = convert_metric_to_imperial(sample_mass, "mass")
        print(f"{sample_mass} kilograms is equal to {imperial_mass:.2f} pounds.")
        imperial_volume = convert_metric_to_imperial(sample_volume, "volume")
        print(f"{sample_volume} liters is equal to {imperial_volume:.2f} US gallons.")
    except ValueError as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)