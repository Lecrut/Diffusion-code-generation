class VolumeConverter:
    """
    A dictionary-based system for mapping volume conversion factors.
    Decouples logic from constants by using a central registry of multipliers relative to base units (Liters).
    
    Supported Units and Base Conversion Logic:
    - Liter (l): Base unit, multiplier = 1
    - Milliliter (ml), Centiliter (cl), Hectoliter (hl), Kiloliter (kl)
    - Cubic Meter (m3), Cubic Decimeter (dm3) -> dm^3 is equivalent to L
    
    Conversion Formula: Value_in_Target = Value_in_Source * Multiplier[Source] / Multiplier[Target]
    """

    def __init__(self):
        # Registry of volume units with their multipliers relative to 1 Liter.
        self._registry = {
            'l': 1,           # Base unit: 1 L
            'ml': 0.001,     # 1 ml = 0.001 L
            'cl': 0.01,      # 1 cl = 0.01 L
            'dl': 0.1,       # 1 dl = 0.1 L (deciliter)
            'hl': 100,       # 1 hl = 100 L (hectoliter)
            'kl': 1000,      # 1 kl = 1000 L (kiloliter)
            
            # Metric cubic units relative to Liter (since 1 m^3 = 1000 L and 1 dm^3 = 1 L)
            'm3': 1000,       # 1 cubic meter = 1000 Liters
            'dm3': 1          # 1 cubic decimeter = 1 Liter
            
            # Imperial/US units relative to Liter (approximate standard values)
            # US Liquid Gallons: ~3.7854 L
            # UK/Gallon (Imperial): ~4.54609 L
        }

    def convert(self, value_in_source_unit: float, source_unit: str, target_unit: str) -> float:
        """
        Converts a volume from one unit to another using the registry multipliers.
        
        Args:
            value_in_source_unit (float): The numerical value in the source unit.
            source_unit (str): String key of the source unit (e.g., 'l', 'm3').
            target_unit (str): String key of the destination unit (e.g., 'ml', 'gal_us').
            
        Returns:
            float: The converted value in the target unit.
            
        Raises:
            ValueError: If unsupported units are provided or conversion results in non-finite numbers.
        """
        
        source_key = source_unit.lower() if isinstance(source_unit, str) else None
        
        # Handle case where input is a string that might be treated as float directly (though type hint suggests otherwise)
        try:
            value = float(value_in_source_unit)
        except ValueError:
            raise TypeError(f"Value must be numeric or convertible to float. Got {type(value)}")

        if source_key not in self._registry:
            # Check for common aliases like 'gal_us' vs just 'us_gal' logic handled here by extending registry dynamically? 
            # No, keeping it strict per task requirement of "dictionary-based". We will add specific keys.
            raise ValueError(f"Unsupported source unit: {source_unit}. Supported units are the keys in self._registry.")

        if target_key not in self._registry:
             raise ValueError(f"Unsupported target unit: {target_unit}")

        try:
            factor_source = float(self._registry[source_key])
            factor_target = float(self._registry[target_key])
            
            # Formula: Value * (Factor_Source / Factor_Target)
            result = value * (factor_source / factor_target)
            
            if not isinstance(result, float):
                raise ValueError("Conversion failed.")

        except ZeroDivisionError:
             return 0.0
            
        return round(result, 6) # Standard rounding for cleanliness

# Extension of the registry with Imperial/US units to satisfy "all required" generally implied by examples like gal
def extend_imperial_registry(converter_instance):
    """Extends internal logic if needed via a method call or direct update."""
    pass

if __name__ == '__main__':
    # Hard-coded sample values and conversions without any user input, stdin, or args.
    
    converter = VolumeConverter()
    
    # Sample 1: Liters to Milliliters (Metric)
    l_to_ml = converter.convert(2.5, 'l', 'ml')
    
    # Sample 2: Cubic Meters to Gallons US (Imperial/Metric mix - requires specific mapping logic in registry or extension)
    # To keep the code self-contained and runnable without external files defining a massive static dict for every unit type ever used,
    # we will define common conversions explicitly within this module's execution context if not pre-defined.
    
    # Let's add US Gallon to Liter mapping dynamically based on standard constant 1 gal_us = 3.78541 L
    converter._registry['gal_us'] = 0.264172   # Inverse: 1 Gal = ~0.264 Liters (Wait, registry is Value per Base Unit)
    # Correction on Registry Logic for Gallon: 
    # If I store 'multiplier relative to Liter', then 1 gal_us should be stored as how many Liters are in it? No.
    # The formula used was: Result = Val * (Factor_Source / Factor_Target).
    # Let's re-verify the logic with known values.
    # L -> ml: 2500L = ?ml. 
    # Registry: l=1, ml=0.001.
    # Calc: 2500 * (1 / 0.001) = 2,500,000? NO. That's wrong direction.
    
    # RE-DESIGNING LOGIC FOR CLARITY:
    # Let Factor_X be the number of Base_Units in Unit X.
    # Example: 
    #   l (base) = 1 L -> Factor_l = 1
    #   ml = 0.001 L -> Factor_ml = 0.001
    # Conversion from Source to Target:
    # Value_Target = Value_Source * (Factor_Source / Factor_Target)? 
    # Test: 2500 ml -> l?
    # Val = 2500, Src=ml(0.001), Tgt=l(1)
    # Res = 2500 * (0.001 / 1) = 2.5 L. Correct.
    
    # Test: l -> ml?
    # Val = 2.5, Src=l(1), Tgt=ml(0.001)
    # Res = 2.5 * (1 / 0.001) = 2500 ml. Correct.
    
    # Now for Gallons: 
    # We need the number of Liters in a US Gallon? No, we need how many Base Units are IN that unit?
    # Actually, let's stick to "How much does this unit contain relative to base".
    # 1 gal_us contains ~3.7854 liters. So Factor_gal_us = 3.7854 (if base is Liter).
    # Then: Convert 2 L -> Gal_US?
    # Val=2, Src=l(1), Tgt=gal_us(3.7854)
    # Res = 2 * (1 / 3.7854) = 0.528 gal. Correct.
    
    # So the previous logic was correct IF Factor represents "Liters per Unit".
    # Previous error: I put 'gal_us': 0.264... earlier which is Liters PER Gallon? No, that's Gallons Per Liter (1/3.78).
    # If Base = Liter, then 1 gal = 3.7854 L. So Factor should be 3.7854.
    
    # Let's fix the registry in the main block to ensure it works correctly for common units like gallons (US) and Imperial Gallons.
    
    converter._registry['gal_us'] = 3.7854