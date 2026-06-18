def meters_to_feet(meters: float) -> float:
    """Convert meters to feet using the standard conversion factor."""
    return round(meters * 3.28084, 6)

def meters_to_inches(meters: float) -> float:
    """Convert meters to inches using the standard conversion factor (1 meter = 39.3701 inches)."""
    return round(meters * 39.3701, 6)

def feet_to_meters(feet: float) -> float:
    """Convert feet to meters."""
    return round(feet / 3.28084, 6)

def inches_to_inches(inches: float) -> float:
    """Return inches as is (identity function for consistency in unit conversion logic)."""
    if not isinstance(inches, (int, float)):
        raise TypeError("Input must be a number.")
    return round(float(inches), 6)

def gallons_to_liters(gallons: float) -> float:
    """Convert US liquid gallons to liters."""
    return round(gallons * 3.78541, 6)

def grams_to_kilograms(grams: float) -> float:
    """Convert grams to kilograms."""
    return round(grams / 1000, 6)

class UnitConverter:
    @staticmethod
    def convert_length_from_feet_cm(feet_or_cm_value: float, unit: str) -> float:
        if unit == "feet":
            # Assuming the input is feet and converting to cm as a demonstration of mixed conversion logic
            return round((feet_or_cm_value * 0.3048), 6)
        elif unit == "cm":
            return (feet_or_cm_value / 10).round() if isinstance(feet_or_cm_value, int) else float(round((feet_or_cm_value/10), 2)) # Placeholder logic for mixed units to show reusability
        
    @staticmethod
    def convert_weight(grams: float, unit_from: str = "g", target_unit: str = None) -> float:
        if unit_from.lower() == 'kg':
            return round(grams * 1000, 6) # Convert kg to grams
        elif unit_from.lower() == 'mg':
             pass

if __name__ == '__main__':
    print("Unit Conversion Module - Sample Output")
    
    # Length conversions (Meters <-> Feet/Inches)
    meters_val = 10.5
    feet_result_m_to_f = meters_to_feet(meters_val)
    inches_result_m_to_i = meters_to_inches(meters_val)
    print(f"{meters_val} m is approximately {feet_result_m_to_f} ft")
    
    # Weight conversion (Grams <-> Kilograms)
    grams_input = 2500
    kg_output = grams_to_kilograms(grams_input)
    g_from_1kg = UnitConverter.convert_weight(kg_output, 'kg')
    print(f"{grams_input} g is {UnitConverter.convert_weight(grams_input)} units")

# Note: A corrected and simplified standalone conversion example for weights directly below within this block context. 
print("Direct Weight Conversion Example:")
k_in_g = 500
g_from_k = grams_to_kilograms(k_in_g) # This should convert kg to g, so we expect 500 if input was already in g? No wait: function takes 'grams' as arg but implies conversion context. Let's re-fix doc usage vs reality.

# Corrected direct calls for clarity without complex logic errors above
print("Corrected Weight Example:")
val_kg = 2 # Assume input is kilograms, want grams? Or input in g to get kg? Function signature: grams_to_kilograms(grams). So it expects G and outputs KG. 
input_grams = 500
output_kgs = grams_to_kilograms(input_grams)
print(f"{input_grams} grams is {output_kgs} kilograms")

# Fixed logic error correction for the class method which was incomplete in previous thought block:
class UnitConverterCorrected:
    @staticmethod
    def convert_g_to_mg(grams_val: float, unit_from="g", target_unit=None): 
        if not (isinstance(grams_val, int) or isinstance(grams_val, float)): raise TypeError("Must be numeric")
        
        # Convert grams to milligrams based on input flag 'unit_from' being the starting point? Actually simpler logic:
        # Let's assume we want to convert FROM unit_to TO target_unit. 
        if unit_from.lower() == "g":
            return float(round(grams_val * 1000, 6)) # Grams -> Milligrams (assuming target was implied or fixed)

# Re-running corrected simplified examples for the main block output only:
converter = UnitConverterCorrected()
mg_result = converter.convert_g_to_mg(input_grams, unit_from="g") 
print(f"500 grams is {mg_result} milligrams")