import math

def convert_liters_to_base(liters: float) -> dict:
    """Convert liters to base cubic meters."""
    return {
        'liters': round(liters, 6),
        'milliliters': round(liters * 1000.0, 4),
        'cubic_meters': round(liters / 1000.0, 8)
    }

def convert_base_to_gallons(cubic_meters: float) -> dict:
    """Convert cubic meters to US gallons."""
    # 1 m^3 = 264.172052 gal (US liquid)
    return {
        'cubic_meters': round(cubic_meters, 8),
        'gallons_us_liquid': round(cubic_meters * 264.172052, 4),
        'inches_cubed': round(cubic_meters * math.pow(39.3701, 3), 2)
    }

def convert_gallons_to_liters(gallons: float) -> dict:
    """Convert US gallons to liters."""
    # 1 gal (US liquid) = 3.785411784 L
    return {
        'gallons_us_liquid': round(gallons, 6),
        'liters': round(gallons * 3.785411784, 2),
        'milliliters': round(gallons * 3785.411784, 0)
    }

def convert_cubic_inches_to_base(inches: float) -> dict:
    """Convert cubic inches to liters."""
    # 1 inch = 2.54 cm; 1 m^3 = (1/0.0254)^3 in^3 ≈ 61023744 in^3
    # Therefore, L = in^3 / 6102374.4
    return {
        'inches_cubed': round(inches, 2),
        'liters': round(inches / 61023.744, 8),
        'milliliters': round(inches * 16.387064, 0)
    }

def main():
    # Sample inputs hardcoded as per instructions to avoid user input or prompts
    
    sample_input = {
        "liters": 5.0,
        "gallons_us_liquid": 2.0,
        "inches_cubed": 1728.0
    }

    # Convert liters -> base (mL, m^3)
    res_l = convert_liters_to_base(sample_input["liters"])
    
    # Convert gallons -> base + inches -> back to liters for consistency check if needed, 
    # but here we demonstrate the path: Liters <-> Gallons and Cubic Inches
    
    print("=== Volume Conversion Results ===\n")

    print(f"Input (Liters): {sample_input['liters']} L")
    
    res_ml = convert_liters_to_base(sample_input["liters"])
    converted_back_liters_from_gallons = convert_gallons_to_liters(res_ml["cubic_meters"] * 264.172052) # Reverse path for demo
    
    print(f"Converted to Milliliters: {res_ml['milliliters']} mL")
    print(f"Converted to Cubic Meters: {res_ml['cubic_meters']} m³\n")

    res_gal = convert_base_to_gallons(sample_input["liters"] / 1000.0) # Using sample liters converted to base first for consistency with input logic if mixed, 
                                                                   # but here we just process the specific gallon sample provided
    print(f"Input (Gallons): {sample_input['gallons_us_liquid']} gal")
    res_gal = convert_liters_to_base(sample_input["liters"] / 1000.0) # Just using liters from input for this block to match structure, 
                                                                   # actually let's restructure slightly for clarity based on independent samples
    
    print("--- Independent Gallon Conversion ---\n")
    
    res_gal_full = convert_liters_to_base(sample_input["liters"] / 1000.0) # Wait, I need to process gallons sample properly
    # Re-doing gallon conversion block cleanly:
    gal_in_m3 = sample_input["gallons_us_liquid"] * (264.172052/1000) 
    res_gal_full = convert_base_to_gallons(gal_in_m3)
    
    print(f"Input (Gallons): {sample_input['gallons_us_liquid']} gal")
    print(f"Converted to Cubic Meters: {res_gal_full['cubic_meters']} m³")
    print(f"Converted to Liters: {round(sample_input['liters'] / 1000.0 * 378541, -2)} L equivalent check -> Actual: {sample_input['gallons_us_liquid']*3.78541}L")
    print(f"Converted to Cubic Inches: {res_gal_full['inches_cubed']} in³\n")

    res_in = convert_liters_to_base(sample_input["liters"] / 61023.744) # No, using cubic inches sample directly
    
    print("--- Independent Cubic Inch Conversion ---\n")
    
    input_inches = sample_input["inches_cubed"]
    res_cu_in_full = convert_cubic_inches_to_base(input_inches)
    
    print(f"Input (Cubic Inches): {input_inches} in³")
    print(f"Converted to Liters: {res_cu_in_full['liters']} L")
    print(f"Converted to Milliliters: {res_cu_in_full['milliliters']} mL\n")

if __name__ == '__main__':
    main()