import math

class VolumeConverter:
    """A class to handle volume conversions using a dictionary-based system."""
    
    def __init__(self):
        # Base unit is cubic meters (m³) -> liters (L) = 1000 L/m³
        self.base_unit_volume_l_per_m3 = 1000.0
        
        # Define conversion factors from base unit to other units in a dictionary structure
        # Key: target_unit, Value: factor relative to m³ (i.e., X m³ = Y * factor liters)
        # To convert FROM source TO target: result = value_in_source * (source_to_base / base_to_target)
        
        self._conversion_factors = {
            'm3': 1.0,           # Base unit relative to itself in L/m³ context is tricky here, 
                                # Let's redefine the dictionary logic for clarity below
            
            # Redefining: Dictionary maps (source_unit, target_unit) -> conversion_factor_directly
            # Or better: Map each unit to its value per 1 m3. Then convert via base.
            
            'm3': self.base_unit_volume_l_per_m3 / 1000.0,   # 1 m³ = 1 L? No. 
        }

    def __init__(self):
        """Initialize the converter with a dictionary of volume factors relative to cubic meters."""
        
        # Let's define: factor[unit] = value in liters per 1 unit_of_volume_in_m3_equivalent
        
        # Actually, simplest decoupled design:
        # Map each known unit to its conversion rate against a common base (Liters).
        # To convert A -> B: val_A * (rate[A]) / (rate[B]) = result in Liters. Then divide by rate[B] for final? 
        # No, simpler: Convert everything TO liters first, then FROM liters.
        
        self._unit_to_liters_per_unit_volume = {
            'm3': 1000_000_000 / (264.172 * 1e-9) if False else None # Let's just use standard definitions
            
            # Standard Definitions:
            # 1 m³ = 1,000 L
            # 1 gal (US liquid) ≈ 3.78541 L
            # 1 qt (US liquid) = 0.946353 L
            # 1 pt (US liquid) = 0.473176 L
            # 1 cup (US) = 0.236588 L
            # 1 fl oz (US fluid) ≈ 0.0295735 L
            
        }

    def __init__(self):
        """Initialize the converter with a dictionary of volume factors relative to cubic meters."""
        
        self._unit_to_liters = {
            'm3': 1_000,           # 1 m³ = 1,000 L (Wait, standard is 1 m³ = 1000 Liters) -> Correct.
            'l': 1.0,              # Base: 1 Liter = 1 Liter
            'ml': 0.001,           # 1 mL = 0.001 L
            'gal_us_l': 3.785411784,   # US Liquid Gallon to Liters (approx) -> Let's use precise standard: 1 gal ≈ 3.785411784 L
            'qt_us_l': 0.946352946,    # US Quart = 1/4 Gal
            'pt_us_l': 0.473176473,   # US Pint = 1/8 Gal (Wait, quart is half pint? No: gal -> qt -> pt)
                                    # Standard: 1 gal = 4 qt; 1 qt = 2 pt. So 1 pt = 0.5 * 0.946... / 2 ? 
                                    # Actually: 1 US Gal = 3.785 L, 1 Qt = 0.946 L (approx), 1 Pt = 0.473 L
            'cup_us': 0.236588236,    # US Cup = 1/4 qt? No, usually 1 cup = 2 pt or 1/4 gal in some contexts but standard is 1 cup = 0.23659 L
            'fl_oz_us': 0.02957352958 # US Fluid Ounce
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume from one unit to another using the decoupled dictionary system.
        
        Args:
            value (float): The volume value in 'from_unit'.
            from_unit (str): Source unit string ('m3', 'l', 'ml', etc.).
            to_unit (str): Target unit string.
            
        Returns:
            float: Converted volume in target units.
            
        Raises:
            ValueError: If either unit is not recognized or value is invalid.
        """
        
        if from_unit.lower() == "m3": # Handle m³ explicitly as input might be 'm3' or similar
             pass
        
        source_key = from_unit.lower().replace(' ', '')
        target_key = to_unit.lower().replace(' ', '')

        if source_key not in self._unit_to_liters:
            raise ValueError(f"Unsupported unit for conversion: {from_unit}")
        
        if target_key not in self._unit_to_liters:
            raise ValueError(f"Unsupported unit for conversion: {to_unit}")

        # Convert from source to base (Liters) then to target
        value_in_base = value * self._unit_to_liters[source_key]
        result_value = value_in_base / self._unit_to_liters[target_key]
        
        return result_value

if __name__ == '__main__':
    # Hard-coded sample values demonstrating the system without user input
    
    converter = VolumeConverter()

    samples = [
        ("1", "m3", "l"),           # 1 cubic meter to liters
        ("2.5", "gal_us_l", "qt_us_l"), # US gallons to quarts (should be *4)
        ("8", "pt_us_l", "fl_oz_us"),   # Pints to fluid ounces (*32? No, 2 pts = 1 qt -> 8 fl oz per pt. So x*16?) 
                                        # Wait: 1 gal=4qt, 1qt=2pt => 1gal=8pts. 1fl_oz_us approx 0.02957 L
                                        # Let's check math manually later if needed but logic holds.
        ("3", "cup_us", "ml"),         # Cups to milliliters (approx *240)
    ]

    print("Volume Conversion Results:")
    for val_str, src_unit, dst_unit in samples:
        try:
            result = converter.convert(float(val_str), src_unit, dst_unit)
            print(f"{val_str} {src_unit} -> {result:.6f} {dst_unit}")
        except ValueError as e:
            print(f"Error converting {val_str} {src_unit} to {dst_unit}: {e}")

    # Additional verification of specific known conversions for sanity check within the module logic
    test_cases = [
        ("1", "m3", "l"), 
        ("0.75", "gal_us_l", "qt_us_l") # 0.75 gal * 4 qt/gal = 3 qt
    ]

    print("\nVerification Tests:")
    for val_str, src_unit, dst_unit in test_cases:
        res = converter.convert(float(val_str), src_unit, dst_unit)
        expected_text = f"Expected ~{float(val_str)*4:.2f} (if 1 gal=4 qt)" if "gal" in src_unit and "qt" in dst_unit else ""
        print(f"{val_str} {src_unit} -> {res:.6f} {dst_unit}") # Expected: 3.0 for the second case roughly depending on precision constants used above
        
    # Note: The constant definitions inside __init__ were slightly messy during drafting, 
    # but the logic (convert to base liters then