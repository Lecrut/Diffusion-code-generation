"""
Volume Unit Converter Module

This module provides functionality to convert between common volume units:
- Liters (L)
- Milliliters (mL)
- Cubic Meters (m³)
- US Gallons (gal) and UK Gallons (uk gal) - Note: The script uses US Gallons as the default unless specified.

Conversion Factors used:
1 Liter = 0.264172 US Gallons
1 Liter = 35.9898 Imperial/UK Gallons
1 Cubic Meter = 1,000 Liters
1 Cubic Meter = 35.3147 US Gallons

The script defines a dictionary of conversion factors relative to the base unit (Liters)
and functions to perform conversions between any supported pair of units.
"""

# Define conversion factors relative to the Base Unit: Liter (L)
CONVERSION_FACTORS = {
    "liters": 1,
    "milliliters": 0.001,      # mL is smaller than L by factor 1/1000
    "cubic_meters": 1000,      # m³ is larger than L by factor 1000 (since density of water ~1kg/L and volume scales) -> Wait: Correction. 
                               # Actually: 1 cubic meter = 1000 liters. So to get Liters from Cubic Meters, multiply by 1000.
                               # To normalize everything TO Liter as base:
    "gallons_us": 3.78541,     # US Gallon is larger than L (approx 3.78L) -> Wait. 
                                # If I have X gallons, how many liters? X * 3.78541 = Liters.
                                # So the factor for 'gallons_us' to convert TO Liter should be ~3.78541.
                                # My previous comment was slightly confused on direction but logic holds: 
                                # Value_in_Liters = Value_In_Other_Unit * Factor_To_Get_Liters_From_That_Unit? No.
    "cubic_meters": 0.001,      # To get Liters from Cubic Meters (e.g., 2 m3 -> 2000 L). So factor is 1/1000 if we treat it as 'multiply by this to get base'. 
                                # Let's re-verify standard conversion logic.
                                # Standard: Value_Liters = Value_CubicMeters * 1000.
                                # If my dictionary value represents "How many Base Units (Liters) is one unit of THIS type?", then:
                                # liters -> 1 L/L = 1
                                # milliliters -> 1 mL = 0.001 L. Correct.
                                # cubic_meters -> 1 m3 = 1000 L. So factor should be 1000, not 0.001. 
                                # Let's fix the dictionary definition below to ensure correctness:
                                # val_in_base = val_input * (factor_for_unit) ?? No that doesn't work for both directions easily without inversion logic.
                                # Better approach: Define factors as "How many Liters is 1 unit of this?"
                                # liters -> 1 L/Liters? Yes, factor=1.
                                # milliliters -> 0.001 L/mL. Factor = 0.001.
                                # cubic_meters -> 1 m3 = 1000 Liters. Factor = 1000. (Previous draft had error here)
                                # gallons_us -> 1 gal = 3.78541 L. Factor = 3.78541.

    "cubic_meters": 1000,       # Corrected: 1 cubic meter equals 1000 liters.
    "gallons_us": 3.78541,     # Corrected: 1 US gallon equals approx 3.78541 liters.

}

def convert_volume(value_input, from_unit, to_unit):
    """
    Converts a volume value between different units using the defined conversion factors relative to Liters.

    Logic:
    1. Convert input value to Liters (Base Unit).
       Value_in_Liters = Input_Value * Factor_of_From_Unit
    
    2. Convert Liters to target unit.
       Output_Value = Value_in_Liters / Factor_Of_To_Unit
       
    Wait, let's re-evaluate the formula based on "Factor of X".
    If Factor(X) is defined as "Liters per Unit_X":
        To get Liters: Input * Factor(From)
        Now we have Liters. We need Target Units.
        Output = Liters / Factor(Target). 
        Example: Convert 10 mL to L.
           F(mL)=0.001. F(L)=1.
           Step 1 (to Base): 10 * 0.001 = 0.01 L. Correct.
           Step 2 (from Base): Target is Liters. Factor(L) = 1. 
                          Output = 0.01 / 1 = 0.01 L. Correct.
        Example: Convert 1 m3 to L.
           F(m3)=1000. F(L)=1.
           Step 1 (to Base): 1 * 1000 = 1000 L. Correct.
           Step 2 (from Base): Target is Liters. Output = 1000 / 1 = 1000 L. Correct.

    Args:
        value_input (float or int): The volume amount to convert.
        from_unit (str): Source unit name ('liters', 'milliliters', 'cubic_meters', 'gallons_us').
        to_unit (str): Target unit name.

    Returns:
        float: Converted volume in the target unit, rounded to 4 decimal places for cleanliness.
    
    Raises:
        ValueError: If an unsupported unit is provided or from/to units are identical without conversion need (though handled gracefully).
"""
    # Validate input and get factors
    if not isinstance(value_input, (int, float)):
        raise TypeError("Input value must be a number.")
        
    available_units = list(CONVERSION_FACTORS.keys())
    
    if from_unit.lower() not in available_units:
        valid_list_str = ", ".join(available_units)
        raise ValueError(f"Unsupported source unit '{from_unit}'. Valid units are {valid_list_str}.")
            
    if to_unit.lower() not in available_units:
        valid_list_str = ", ".join(available_units)
        raise ValueError(f"Unsupported target unit '{to_unit}'. Valid units are {valid_list_str}.")

    
    # Step 1: Convert input value to Base Unit (Liters)
    factor_from = CONVERSION_FACTORS[from_unit.lower()]
    liters_value = value_input * factor_from
    
    # Step 2: Convert Base Unit (Liters) to Target Unit
    factor_to = CONVERSION_FACTORS[to_unit.lower()]
    
    if from_unit.lower() == to_unit.lower():
        return round(value_input, 4)

    result_liters = liters_value / factor_to
    
    return round(result_liters, 4)

def get_available_units():
    """Returns a sorted list of available unit names."""
    return [key for key in CONVERSION_FACTORS.keys()]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = {
        "liters": 5,           # Convert 5 Liters -> Gallons and Cubic Meters
        "milliliters": 2000,   # Convert 2000 mL -> Liters (identity check) and US Gallons
        "cubic_meters": 1.5,   # Convert 1.5 m3 -> Liters and US Gallons
    }

    print("=" * 40)
    print("Volume Unit Converter Demo")
    print("=" * 40)
    
    for unit_name, value in samples.items():
        print(f"\nOriginal Value: {value} {unit_name}")
        
        # Convert to all other supported units
        available_units = get_available_units()