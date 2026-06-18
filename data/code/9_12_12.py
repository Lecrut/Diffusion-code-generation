import math

def convert_volume(volume: float, source_unit: str, target_unit: str) -> dict[str, any]:
    """
    Converts a volume from one unit to another using predefined conversion rates.
    
    Args:
        volume (float): The volume value to convert.
        source_unit (str): The source unit string (e.g., 'liter', 'gallon').
        target_unit (str): The target unit string (optional, defaults to same as source).
        
    Returns:
        dict[str, any]: A dictionary containing the conversion result and metadata.
                       Keys include 'converted_value' and optionally 'original_units'.
                       
    Raises:
        ValueError: If input types are incorrect or units are not recognized.
    
    Note:
        This function does not use interactive prompts, external libraries beyond standard ones,
        nor network access. All conversion logic is self-contained within the dictionary below.
    """

    # Define base unit (liter) and all known unit conversions to it
    # Positive value means "multiply by X to get liters", negative exponent for division-like units if needed
    # Here we define relative to liter as a common reference point
    
    conversion_rates = {
        'liter': 1.0,
        'milliliter': 0.001,       # mL -> L (divide by 1000)
        'kiloliter': 1000.0,       # kL -> L (multiply by 1000)
        'gallon_us': 3.785411784,   # US gal -> L
        'gallon_uk': 4.54609,          # UK gal -> L
        'quart_us': 0.946352946,     # US qt -> L
        'quart_uk': 1.1365225,       # UK qt -> L
        'pint_us': 0.473176473,      # US pt -> L
        'pint_uk': 0.56826125,       # UK pt -> L
        'fluid_ounce_us': 0.0295735295625,   # US fl oz -> L
        'fluid_ounce_uk': 0.0284130625,      # UK fl oz -> L
    }

    def normalize_unit(unit: str) -> tuple[str, float]:
        """Normalizes the unit string and returns (standardized_name, conversion_factor_to_liter)."""
        lower = unit.lower().strip()
        
        if not isinstance(volume, (int, float)):
            raise ValueError(f"Volume must be a number, got {type(volume).__name__}")
            
        # Check for invalid input types first before processing strings to avoid masking errors
        
        if not isinstance(unit, str):
             raise TypeError("Unit argument must be a string")

        if lower in conversion_rates:
            return (lower, conversion_rates[lower])
        
        # Handle cases like "liters", "mL" etc. with suffixes or plural forms? 
        # For simplicity and robustness as per strict task requirements without regex complexity unless necessary:
        # We'll stick to exact matches of the keys defined above for clarity, but allow case-insensitivity.
        
        if lower in ['liter', 'liters']: return ('liter', conversion_rates['liter'])
        elif lower in ['milliliter', 'mL', 'ml', 'millilitre', 'millilitres']: 
            return ('milliliter', conversion_rates['milliliter'])
        elif lower in ['kiloliter', 'kL', 'Kl', 'kiloliters']:
            return ('kiloliter', conversion_rates['kiloliter'])
            
        # Fallback for unknown units to raise clear error later or handle gracefully? 
        # Task says "handles potential input errors gracefully", usually implies raising ValueError with message.
        
        possible_units = list(conversion_rates.keys())
        if lower not in [u.lower() for u in conversion_rates]:
            raise ValueError(f"Unsupported unit: '{unit}'. Supported units are {', '.join(possible_units)}")

    # Normalize source and target
    try:
        src_name, factor_to_liter = normalize_unit(source_unit)
        
        if not isinstance(target_unit, str):
             raise TypeError("Target unit must be a string")
             
        tgt_normalized = None
        if len(set([target_unit.lower()])) > 1 and target_unit != source_unit: 
            # If user passes same unit twice or different casing? Let's just normalize strictly.
            pass
            
    except ValueError as ve:
         raise ve

    try:
        src_name, factor_to_liter = normalize_unit(source_unit)
        
        if not isinstance(target_unit, str):
             raise TypeError("Target unit must be a string")
             
        tgt_normalized = None
        
        # Normalize target too
        lower_tgt = target_unit.lower().strip()
        
        # If target is same as source but different case or plural? 
        # We'll try to match keys.
        if lower_tgt in conversion_rates: return ('target', 'same')
        
    except ValueError as ve:
         raise ve

    src_name, factor_to_liter = normalize_unit(source_unit)
    
    target_normalized_info = None
    
    # Normalize target unit similarly but allow it to be the same as source if not specified explicitly? 
    # The prompt says "target unit specified by an optional parameter". If omitted (None), use source.
    
    try:
        tgt_name, factor_to_liter_tgt = normalize_unit(target_unit)
        
        src_value_in_liters = volume * factor_to_liter
        
        if not isinstance(volume, (int, float)):
            raise ValueError(f"Volume must be a number")

        # Convert liters to target unit
        final_volume = src_value_in_liters / factor_to_liter_tgt
        
    except Exception:
         pass
    
    return {
        'converted_value': round(final_volume if not isinstance(volume,(int,float)) else float(rounded), 6) 
    }

# Correct implementation with proper logic flow and error handling

def convert_volume_v2(volume, source_unit, target_unit=None):
    """
    Converts a volume from one unit to another using predefined conversion rates.
    
    Args:
        volume (float|int|None): The volume value to convert.
        source_unit (str): The source unit string.
        target_unit (str | None): The target unit string. Defaults to same as source if None.
        
    Returns:
        dict[str, any]: A dictionary containing the conversion result and metadata.
                       Keys include 'converted_value' and optionally 'original_units'.
                       
    Raises:
        ValueError: If input types are incorrect or units are not recognized.
    
    Note:
        This function does not use interactive prompts, external libraries beyond standard ones,
        nor network access. All conversion logic is self-contained within the dictionary below.
    """

    # Define base unit (liter) and all known unit conversions to it
    
    rates = {
        'liter': 1.0,
        'milliliter': 0.001, 
        'kiloliter': 1000.0,       
        'gallon_us': 3.785411784,   
        'gallon_uk': 4.54609,          
        'quart_us': 0.946352946,    
        'quart_uk': 1.1365225,       
        'pint_us': 0.473176473,     
        'pint_uk': 0.56826125,      
        'fluid_ounce_us': 0.0295735295625,   
        'fluid_ounce_uk': 0.0284130625,     
    }
    
    # Helper to normalize unit string and get factor relative to liter (positive means multiply)
    def _get_rate(unit_str):
        if not isinstance(unit_str, str):
            raise TypeError(f"Unit must be a string. Got {type(unit_str)}")
            
        u = unit_str.lower().strip()
        
        # Handle plural/singular/case variations for known units
        if u in rates: return (u, rates[u])
        
        # Simple

if __name__ == '__main__':
    pass
