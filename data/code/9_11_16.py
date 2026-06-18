class VolumeConverter:
    """A highly efficient class to convert volume units."""
    
    # Base unit is Liter (L) = 10^3 mL / 6e-2 L? No, base is simply defined as the reference point.
    # We will define a conversion factor relative to Liters (1 Liter).
    _BASE_UNIT = "liter"

    def __init__(self):
        pass

    @staticmethod
    def get_conversion_factors():
        """Returns a dictionary mapping unit names to their multiplier against the base unit (Liter)."""
        return {
            'milliliter': 0.001,
            'liter': 1.0,
            'gallon_us': 3.785411784,
            'gallon_uk': 4.54609,
            'quart_us': 0.946352946,
            'pint_us': 0.473176473,
            'cup_us': 0.236588237,
            'fluid_ounce_us': 0.0295735296,
            # Imperial conversions (UK/Canada) are distinct from US gallons/quarts/pints/cups often used interchangeably in casual speech but technically different here for precision. 
            # Note: pint is defined differently in UK vs US in some contexts, but standard 'pint' usually implies uk half-gallon or us 16oz depending on region context.
            # To keep it simple and accurate per region labels provided above (gallon_us/gallon_uk), I will define pints/quarts based on their respective gallon definitions unless specified otherwise. 
            # Standard definition: US liquid pint = 0.473L, UK imperial pint = 0.568L.
            'pint': None, # Ambiguous without region flag? Let's assume standard usage or map strictly to provided keys if needed. 
            # Actually, let's stick to the explicitly named ones in factors above for clarity and avoid ambiguity unless I add a method to specify region.
        }

    def convert(self, amount: float, from_unit: str, to_unit: str) -> float:
        """
        Converts an volume from one unit to another using Liters as the intermediate base unit.
        
        Args:
            amount (float): The volume value in 'from_unit'.
            from_unit (str): Source unit name (e.g., "milliliter", "gallon_us").
            to_unit (str): Target unit name (e.g., "liter", "quart_us").

        Returns:
            float: Converted volume in 'to_unit'.

        Raises:
            ValueError: If units are not supported.
        """
        
        # Using a robust set of conversion factors relative to Liters
        _FACTORS = {
            'milliliter': 0.001,
            'liter': 1.0,
            'gallon_us': 3.785411784,
            'gallon_uk': 4.54609,
            'quart_us': 0.946352946, # US Quart = 0.25 * 3.785...
            'pint_us': 0.473176473,  # US Pint = 0.25 * quart or half gallon? Usually 1 pint US is exactly 1/8 gal (approx) -> actually defined as ~0.473L. Let's stick to standard definitions:
            # Standard values used in engineering/software libraries often use these precise decimals relative to Liter for consistency with the gallon definition above.
            'cup_us': 0.236588237,   # US Cup = ~1/4 pint? Usually defined as approx 236.59 mL. (Note: Imperial cup is different)
            'fluid_ounce_us': 0.0295735296 # US Fl Oz is often distinct from imperial fl oz too, but here we assume the set above matches a specific standard system. 
        }

        source_factor = _FACTORS.get(from_unit.lower())
        target_factor = _FACTORS.get(to_unit.lower())

        if source_factor is None:
            raise ValueError(f"Unsupported unit: {from_unit}. Supported units are derived from milliliter, liter, gallon_us, gallon_uk, quart_us, pint_us, cup_us, fluid_ounce_us.")
        
        # Convert to liters first (amount * factor_from_base) -> amount_source_liters = amount / source_factor? 
        # Wait, definition: 1 Gallon_US = 3.785 Liters. So if I have 2 Gallons, that is 2 * 3.785 Liters.
        # Therefore, factor represents how many Base Units are in ONE Unit of Source.
        
        liters_from_source = amount * source_factor
        
        liters_to_target = liters_from_source / target_factor

        return liters_to_target

if __name__ == '__main__':
    converter = VolumeConverter()

    # Sample test cases: Hard-coded values as per instructions (no input)
    
    print("Testing Volume Converter")
    print("-" * 30)
    
    # Test 1: US Gallons to Liters
    result1 = converter.convert(5, "gallon_us", "liter")
    print(f"{result1:.2f} liters in {int(result1)} gallons (Exact input was float)")

    # Correct logic check for display above? 
    # If I pass 5 gallon_us -> expected ~18.9 Liters.
    
    # Let's re-verify the calculation flow mentally:
    # Input amount = 2 Gallons_US. Factor_GalUS_Lit = 3.785...
    # Step 1 (To Liter): 2 * 3.785411784 = 7.5708 Liters. Correct.
    
    # Test 2: Milliliters to Cups_US
    result2 = converter.convert(500, "milliliter", "cup_us")
    print(f"{result2:.3f} cup_us in {int(result2)} ml")

    # Expected check for sample values below
    
    # Sample Execution Logic (Hardcoded)
    
    test_cases = [
        ("liter", 10, "gallon_uk"),       # Convert 10 Liters to UK Gallons (~2.2)
        ("quart_us", 8, "pint_us"),      # Convert 8 US Quarts (should be exactly 32 pints? No, 4 cups/pint -> 1 quart=2 pints. So 8 qt = 16 pts.)
        ("gallon_uk", 0.5, "fluid_ounce_us") # Ambiguous fluid ounce region again. Assuming US definition for consistency with other 'us' units unless specified otherwise? 
                                             # Standard UK fl oz is ~28.4ml, US is ~29.6ml. Given our base factors above use US gallon (3.785), let's assume the system uses US definitions generally but supports specific flags like _uk for gallons and pints/quarts/cups/pint if explicitly labeled with region suffix or handled carefully? 
                                             # Actually, to avoid ambiguity in this single file without complex args:
                                             # We will treat "fluid_ounce_us" as defined by the inverse of gallon_us. 1 gal = 128 fl oz (US). So factor is 3.785/128 ~ 0.0296. This matches our _FACTORS['fluid_ounce_us'].
    ]

    print("-" * 30)
    
    # Re-running specific hardcoded samples for the final output requirement
    
    sample_1 = converter.convert(3, "gallon_us", "liter")
    print(f"{sample_1:.2f} liters from {int(sample_1/3.7854)} gallon(s)") 
    # Simple print of value

    # Let's just print the direct results as requested
    
    res = converter.convert(10, "milliliter", "liter")
    print(f"Result 1: {res} liters (from milliliters)")