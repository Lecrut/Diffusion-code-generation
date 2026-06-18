class VolumeConverter:
    """A highly optimized class to convert volumes between common units."""
    
    # Base unit is Liter (L). Conversion factors relative to 1 Liter.
    # Positive factor means X Unit = 1 L
    # Negative factor logic handled in conversion method, but stored as magnitude for clarity.
    FACTORS_TO_BASE = {
        'liters': 1.0,          # Base unit: 1 Litre = 1 Litre
        'milliliters': 1000.0, # 1 Liter = 1000 Millilitres
        'kiloliters': 0.001    # 1 Kilolitre = 0.001 L (or 1/1000) -> Actually defined as: Input in KiloL to get Base? No, let's standardize input unit factor relative to base output value of 1 Litre for the conversion logic below.
        # Correction on semantic definition for easier math: 
        # We want a dictionary where Key is Source Unit, Value is Multiplier applied to Source Volume to get Litres.
    }

    # Corrected Factors Dictionary (Source -> Multiplication Factor to get Liters)
    TO_BASE_FACTORS = {
        'liters': 1.0,
        'milliliters': 1e-3,   # mL * (1/1000) = L? No. 
                            # Let's stick to: Result_Litres = Source_Value * Factor_To_Base_Factor
                            # If I have 5 ml, factor should be 0.001. So 5 * 0.001 = 0.005 L. Correct.
        'kiloliters': 1e3,     # kL * 1000 = L? No. 
                            # If I have 2 kL, factor should be 1000. So 2 * 1000 = 2000 L. Correct.
    }

    def __init__(self):
        pass
    
    @staticmethod
    def get_supported_units():
        return list(VolumeConverter.TO_BASE_FACTORS.keys())

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Converts a volume from one unit to another.
        
        Args:
            value (float): The volume amount.
            from_unit (str): Source unit string (case-insensitive).
            to_unit (str): Target unit string (case-insensitive).
            
        Returns:
            float: Converted volume in the target unit.
            
        Raises:
            ValueError: If units are unsupported or invalid.
        """
        from_lower = from_unit.lower()
        to_lower = to_unit.lower()

        if from_lower not in VolumeConverter.TO_BASE_FACTORS:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        
        # Validate target exists as a supported unit (even for base conversion)
        if to_lower == 'base': 
             self.__convert_to_base(value, from_lower)
             return value
        
        if to_lower not in VolumeConverter.TO_BASE_FACTORS:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        # Strategy: Convert Source -> Base (Liters), then Base -> Target.
        
        liters = volume * VolumeConverter.TO_BASE_FACTORS[from_lower]
        return liters / VolumeConverter.TO_BASE_FACTORS[to_lower]

# Note on the above logic regarding factors:
# TO_BASE_FACTORS maps [InputUnit, FactorToGetLitres]. 
# Liter to Liters: 100mL * (1/1000) = 0.1 L? Wait.
# Let's redefine FACTORS_TO_LITERS for absolute clarity in comments within code logic if needed, but let's just use clean math here.

    @classmethod
    def _get_factors_to_liters(cls):
        """Returns the multiplier to convert a specific input unit value directly into Litres."""
        return {
            'liters': 1.0,
            'milliliters': 0.001,   # mL -> L (divide by 1000)
            'kiloliters': 1000.0,   # kL -> L (multiply by 1000)
        }

def convert_volume(volume: float, from_unit: str, to_unit: str):
    """Helper function exposed for direct use if preferred over class instantiation."""
    
    factors = VolumeConverter._get_factors_to_liters()
    
    # Step 1: Convert Source to Litres
    liters_value = volume * (factors[from_unit.lower()] / factors[to_unit.lower()] )

def main():
    converter = VolumeConverter()
    
    print("Testing Optimized Volume Converter")
    print("-" * 20)

    # Test Case 1: Milliliters to Liters
    result_m_to_l = converter.convert(500, "milliliters", "liters")
    expected = 0.5
    assert abs(result_m_to_l - expected) < 1e-9, f"Test failed for mL->L: got {result_m_to_l}"
    
    # Test Case 2: Kiloliters to Liters
    result_k_to_l = converter.convert(2.5, "kiloliters", "liters")
    expected = 2500.0
    assert abs(result_k_to_l - expected) < 1e-9, f"Test failed for kL->L: got {result_k_to_l}"

    # Test Case 3: Liters to Kiloliters (Inverse direction check on factors logic implicitly handled by division)
    result_l_to_k = converter.convert(500.0, "liters", "kiloliters")
    expected = 0.5
    
    print(f"500 mL -> {result_m_to_l} L")
    assert abs(result_m_to_l - 0.5) < 1e-9

    result_k_to_grams_of_water_approximation = converter.convert(2, 'kiloliters', 'liters') # Just to show kL->L works
    
    print(f"2.5 kL -> {result_k_to_l} L")
    
    # Edge case: Same unit conversion (should return original)
    result_same = converter.convert(100, "milliliters", "milliliters")
    assert abs(result_same - 100) < 1e-9

    print("All tests passed successfully.")

if __name__ == '__main__':
    main()