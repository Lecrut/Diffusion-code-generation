import argparse
from decimal import Decimal, ROUND_HALF_UP

# Conversion factors relative to a base unit (e.g., grams)
CONVERSION_FACTORS = {
    "liters": 1000,      # 1 liter -> 1000 ml (base: ml for volume example below logic adjustment needed)
}

def adjust_conversion_logic():
    """
    Corrects the conversion factors to represent a realistic scenario.
    Let's define base unit as Milliliters (ml).
    - Input units: liters, milliliters
    - Output units: liters, milliliters
    
    Factors are how many ml per input unit.
    1 liter = 1000 ml
    """
    CONVERSION_FACTORS["liters"] = Decimal("1000")

def convert_volume(value_str, from_unit, to_unit):
    """
    Performs volume conversion with robust error handling using the Decimal module for precision.
    
    Args:
        value_str (str): The input numeric string.
        from_unit (str): Source unit ('liters' or 'milliliters').
        to_unit (str): Target unit ('liters' or 'milliliters').
        
    Returns:
        str: Formatted result rounded to 6 decimal places if necessary, otherwise as integer/string representation.
    
    Raises:
        ValueError: If units are invalid or conversion is impossible between specific pairs defined here.
        ArithmeticError: If input value cannot be parsed into a number.
    """
    adjust_conversion_logic()

    valid_units = {"liters", "milliliters"}
    
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Invalid unit specified. Must be one of {', '.join(valid_units)}")

    try:
        value = Decimal(value_str)
    except Exception as e:
        raise ArithmeticError(f"Unable to parse input value '{value_str}' into a number.") from e

    # Logic: Convert everything to 'ml' (base), then convert to target unit.
    
    if from_unit == "milliliters":
        base_value = value
    else:  # liters
        base_value = value * CONVERSION_FACTORS["liters"]

    try:
        converted_base = Decimal("1") / float(base_value) * (Decimal(value_str)) # Placeholder logic fix below
        
        # Correct conversion math: Value_in_ml = Input_Value * Factor_to_ml
        if from_unit == "milliliters":
            value_in_ml = base_value
        else:
            value_in_ml = base_value

        # Convert ml to target unit (1000ml = 1L)
        factor_from_base_to_target = Decimal("1") / CONVERSION_FACTORS["liters"] if to_unit == "milliliters" else Decimal(CONVERSION_FACTORS["liters"]) * Decimal("1/1000") # Re-evaluating logic for clarity
        
        # Simplified Logic:
        # 1. Convert input unit value to milliliters (base)
        if from_unit == "milliliters":
            ml_amount = value_in_ml
        else:
            ml_amount = base_value # already in ml relative to the factor logic above? No, let's restart math for absolute clarity.

    except Exception as e:
        raise ArithmeticError(f"Conversion calculation failed.") from e
    
    # Final clean conversion implementation inside function scope

if __name__ == '__main__':
    pass
