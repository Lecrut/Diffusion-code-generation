# Volume Unit Converter Module
# Converts between liters (L), milliliters (mL), cubic meters (m³), 
# gallons (US liquid), and cubic inches (in³).

def convert_volume(value: float, from_unit: str) -> dict:
    """
    Convert a given volume value to all other supported units.
    
    Args:
        value (float): The numerical value of the volume.
        from_unit (str): Source unit ('L', 'mL', 'm3', 'gal', 'in^3').
        
    Returns:
        dict: Dictionary containing values in all supported units.
    """
    
    # Base conversion factor to Liters for each source unit
    base_conversion_factors = {
        "L": 1,
        "mL": 0.001,      # Convert mL to L by dividing by 1000 (or multiplying by 0.001)
        "m3": 1000,       # Convert m³ to L by multiplying by 1000
        "gal": 3.78541,   # US gallons to Liters conversion factor (~3.78541 L/gal)
        "in^3": 61.0237,  # Cubic inches to Liters conversion factor (~61.0237 in³/L)
    }

    if from_unit not in base_conversion_factors:
        raise ValueError(f"Unsupported unit '{from_unit}'. Supported units: L, mL, m^3, gal, in^3")

    # Convert the input value to Liters (the reference standard for this module)
    liters = value * base_conversion_factors[from_unit]

    # Calculate values for all other units from the calculated Liter value
    conversions = {
        "L": round(liters, 6),
        "mL": round(liters * 1000, 2),       # Liters to milliliters (multiply by 1000)
        "m3": round(liters / 1000, 8),         # Liters to cubic meters (divide by 1000)
        "gal": round(liters / base_conversion_factors["gal"], 6),   # Liters to gallons
        "in^3": round(liters * base_conversion_factors["in^3"], 2)    # Liters to cubic inches
    }

    return conversions

def main():
    """
    Main function demonstrating the converter with hard-coded sample values.
    Runs without user input, command-line arguments, or network access.
    """
    
    samples = {
        "L": 5,               # Sample: 5 Liters
        "mL": 2000,           # Sample: 2000 Milliliters (should equal 2 L)
        "m3": 1.5,            # Sample: 1.5 Cubic Meters
        "gal": 10,            # Sample: 10 US Gallons
        "in^3": 4789          # Approximation for 1 gallon in cubic inches (~4789)
    }

    print("=== Volume Unit Conversion Demo ===")
    print()
    
    for key, value in samples.items():
        source_name = f"{key.upper().replace('m3', 'M^3').replace('^', '')}" if not isinstance(key, str).split()[0] else " ".join(key.split()) # Simple string processing to make names readable
        
        # Construct a clean display name for the key based on its original representation
        unit_symbol = None
        if key == "L": unit_symbol = "Liters"
        elif key == "mL": unit_symbol = "Milliliters"
        elif key == "m3": unit_symbol = "Cubic Meters"
        elif key == "gal": unit_symbol = "Gallons (US)"
        else: unit_symbol = "Cubic Inches"

        print(f"Converting {value} {unit_symbol}:")
        
        try:
            result_values = convert_volume(value, source_name)
            
            # Print the converted values in a neat format
            for target_unit_name, final_value in result_values.items():
                if target_unit_name == "L":
                    unit_str = "Liters"
                elif target_unit_name == "mL":
                    unit_str = "Milliliters"
                elif target_unit_name == "m3":
                    unit_str = "Cubic Meters"
                elif target_unit_name == "gal":
                    unit_str = "Gallons (US)"
                else:
                    unit_str = "Cubic Inches"
                
                print(f"  -> {final_value} {unit_str}")
            
            # Add a separator for clarity between samples if multiple are printed, 
            # though here we process them sequentially.
        except Exception as e:
            print(f"Error converting from {source_name}: {e}")

    print()
    print("Conversion complete.")

if __name__ == '__main__':
    main()