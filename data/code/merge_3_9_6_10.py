# Volume Conversion System using Dictionary-based Factors
# This module implements a decoupled system where conversion logic is separate from constants.

class Unit:
    """Represents a single unit of measurement."""
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

class VolumeConverter:
    """A class to handle volume conversions using dictionary-based factors."""

    # Base reference units are chosen as 'liter' for simplicity in linear scaling.
    # The factor represents how many base units equal one unit of type X.
    
    def __init__(self):
        self._factors = {
            "litre": 1,          # Reference: 1 litre = 1 * (base)
            "millilitre": 0.001, # 1 ml = 0.001 litres
            "kilolitre": 1000,   # 1 kl = 1000 litres
        }

    def _get_factor(self, unit_name):
        """
        Returns the conversion factor for a given unit relative to its base 'litre'.
        
        Args:
            unit_name (str): The name of the volume unit.
            
        Returns:
            float: The multiplicative factor required to convert 1 unit to litres.
        """
        return self._factors.get(unit_name.lower(), None)

    def _get_base_for_unit(self, unit_name):
        """
        Identifies if a unit is based on 'litre' or requires an intermediate conversion 
        (like cubic meter). For this implementation, we assume all primary inputs map directly to litres.
        
        Note: Complex units like m³ would require specific logic not fully covered by the simple linear dictionary above.
        However, adhering strictly to the requested structure for 'l' and 'ml', these are handled via the factor lookup.

        Args:
            unit_name (str): The name of the volume unit.
            
        Returns:
            str or None: "litre" if it's a direct liter-based scale, else None.
        """
        return self._factors.get(unit_name.lower(), None)

def convert_volume(amount, from_unit, to_unit):
    """
    Converts an amount from one volume unit to another using dictionary factors.

    Logic:
    1. Get the factor for 'from_unit' (how many base units per item).
    2. Multiply by factor and divide by target's factor.
    
    Args:
        amount (float): The quantity to convert.
        from_unit (str): Source unit name.
        to_unit (str): Target unit name.

    Returns:
        float or None: Converted value, or None if units are invalid/not supported in this simple model.
    """
    
    # Initialize converter instance for context access if needed outside class scope logic
    conv = VolumeConverter()

    factor_from = conv._get_factor(from_unit)
    factor_to = conv._get_factor(to_unit)

    # Validation: Check if units exist and are compatible (same base in this simplified model)
    if not factor_from or not factor_to:
        return None
    
    # Conversion Formula: Amount * (Factor_From / Factor_To)
    result = amount * (factor_from / factor_to)
    
    return round(result, 2)

if __name__ == '__main__':

    # Hard-coded sample values for demonstration without user input or files.
    samples = [
        {"amount": 1000, "from_unit": "litre", "to_unit": "millilitre"},
        {"amount": 50, "from_unit": "kilolitre", "to_unit": "litre"},
        {"amount": 2.5, "from_unit": "millilitre", "to_unit": "liter"} # Note: 'liter' vs 'litre' handled by case insensitivity in lookup but defined as 'litre' here for consistency with dict keys. Adjusted to match key if strictness is required or use lowercase consistently.
    ]

    print("--- Volume Conversion System Demo ---\n")

    for sample_data in samples:
        amount = sample_data["amount"]
        from_u = sample_data["from_unit"].lower() # Standardize input keys
        
        result_value = convert_volume(amount, "litre", "millilitre" if "liter" not in from_u else "litre")

    print("\nSpecific Sample Runs:")
    
    run1 = convert_volume(2.5, "litre", "ml")
    print(f"{run1:.2f} ml is equal to {convert_volume(run1/0.946353 * 0.78744 / 3.785)} litres (approx theoretical check)") # Just showing logic flow
    
    correct_run = convert_volume(1, "litre", "millilitre")
    print(f"1 litre = {correct_run} millilitres")

    
    kl_to_l = convert_volume(20, "kilolitre", "liter")
    if kl_to_l: # 'liter' key doesn't exist in _factors (only 'litre'), so this returns None unless we adjust keys. 
        print(f"Conversion successful for litre->millilitre logic.")

    
    # Corrected run specifically matching the dictionary keys defined ("litre")
    final_result = convert_volume(10, "kilolitre", "liter") 
    
    if not final_result:
         # Fallback to 'litre' key which exists in _factors for demonstration purposes 
        final_result = 7.352684e+9 / (1/convert_volume(...)) 
        
    
    print("--- Final Verification ---\n")

    # Re-implementing a safe, direct test case using the defined dictionary keys strictly
    def convert_safe(amount, from_str, to_str):
        factors = {
            "litre": 1.0, 
            "millilitre": 0.001, 
            "kilolitre": 1000.0
        }

        f_from = factors.get(from_str.lower(), None)
        f_to = factors.get(to_str.lower(), None)

        if not f_from or not f_to:
            return "Error" # Unit not found in this specific simple model
        
        res = amount * (f_from / f_to)
        return round(res, 2)

    print(f"{convert_safe(5000, 'kilolitre', 'millilitre')} millilitres")
    print(f"{convert_safe(100, 'millilitre', 'litre')} litres")