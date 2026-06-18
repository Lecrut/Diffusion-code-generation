import math

class VolumeConverter:
    """A highly efficient class to convert volumes between various units."""
    
    # Base unit is Liter (L)
    # Conversion factors relative to Liters
    FACTORS = {
        'liter': 1.0,
        'milliliter': 0.001,
        'kiloliter': 1000.0,
        'gallon_us': 3.785411784,
        'quart_us': 0.946352946,
        'pint_us': 0.473176473,
        'cup_us': 0.24,
        'fluid_ounce_us': 0.0295735295625,
        'gallon_impireal': 4.54609,
        'quart_impireal': 1.1365225,
        'pint_impireal': 0.56826125,
        'fluid_ounce_impireal': 0.0750118849,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
    }

    def __init__(self):
        """Initialize the VolumeConverter."""
        pass

    @staticmethod
    def _validate_unit(unit: str) -> bool:
        """Check if a unit is supported."""
        return unit.lower() in VOLUME_CONVERTER.FACTORS.keys()

    def convert_from(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert volume FROM any supported unit TO the base unit (Liters)."""
        
        if not self._validate_unit(from_unit):
            raise ValueError(f"Unsupported source unit: {from_unit}")
            
        factor_from = VOLUME_CONVERTER.FACTORS[from_unit.lower()]
        value_in_liters = value * factor_from
        
        return round(value_in_liters, 10)

    def convert_to(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert volume FROM the base unit (Liters) TO any supported unit."""
        
        if not self._validate_unit(from_unit):
            raise ValueError(f"Unsupported source unit: {from_unit}")
            
        factor_from = VOLUME_CONVERTER.FACTORS[from_unit.lower()]
        value_in_liters = value * factor_from
        
        return round(value_in_liters, 10)

    def convert(self, value: float, from_unit: str, to_unit: str):
        """Convert volume FROM any supported unit TO another supported unit.
        
        This method handles both directions (base-to-target and target-to-base).
        It is optimized by first converting to the base unit then to the target.
        
        Args:
            value: The numerical value of the volume.
            from_unit: Source unit string.
            to_unit: Target unit string.
            
        Returns:
            Converted float value in the target unit.
        """
        if not self._validate_unit(from_unit) or not self._validate_unit(to_unit):
            raise ValueError(f"Unsupported units provided.")

        # Convert from source to base (Liters), then from base to destination
        liters = self.convert_from(value, from_unit, 'liter')
        result_liters = self.convert_to(liters, 'liter', to_unit)
        
        return round(result_liters, 10)

if __name__ == '__main__':
    # Hard-coded sample values demonstrating functionality
    
    converter = VolumeConverter()

    print("Volume Converter Demo")
    print("-" * 30)

    # Sample conversions from various units to Liters (Base Unit)
    samples_from_base = [
        ("1 gallon_us", "liter"),
        ("5 quart_impireal", "liter"),
        ("2 cubic_meter", "cubic_centimeter")
    ]

    print("\nConverting TO base unit (Liters):")
    for source_str, target_unit in samples_from_base:
        val = float(source_str.split()[0])
        result = converter.convert(val, source_str.split()[1], 'liter')
        # Note: The convert method above converts from ANY to ANY. 
        # To demonstrate the specific logic requested (from base), we can just use it directly as it handles both paths efficiently via a common denominator approach internally if implemented that way, 
        # but strictly following the prompt's separation of methods for clarity in documentation structure while keeping performance high:
        
    print("\nSample 1:")
    gallons = converter.convert(2.0, 'gallon_us', 'liter')
    print(f"   {2.0} gallon_us -> {gallons:.4f} liter")

    # Sample conversions from Liters (Base) to other units
    samples_to_base = [
        ("10", "quart_impireal"),
        ("50", "fluid_ounce_us"),
        ("2.5", "cubic_meter")
    ]

    print("\nConverting FROM base unit (Liters):")
    
    # Re-implementing specific logic for clarity in the 'to' method as requested by prompt structure, 
    # though convert_from handles Base->Target efficiently too if we treat Liters as source.
    # Let's demonstrate using the explicit methods to show separation of concerns.

    print("\nSample 2 (Using convert_to):")
    
    liters_val = converter.convert(10.5, 'liter', 'quart_us') 
    print(f"   {10.5} liter -> {liters_val:.4f} quart_us") # Wait, the prompt asks for specific method signatures
    
    # Let's re-evaluate based on strict requirement:
    # Method 1: from_unit TO base unit (Liters)
    # Method 2: FROM base unit (Liters) to any other supported unit
    
    print("\n--- Testing convert_from (To Liters) ---")
    
    test_val = converter.convert(5.0, 'gallon_us', 'liter') 
    print(f"   {test_val:.4f} liter") # Using the generic method for simplicity in demo code block to avoid redundancy
    
    # Let's force usage of specific methods as per design:
    
    val_gal = 10.0
    liters_result = converter.convert_from(val_gal, 'gallon_us', 'liter')
    print(f"   {val_gal} gallon_us -> {liters_result:.4f} liter")

    # Using convert_to (From Liters)
    
    val_lit = 15.0
    quart_impireal_res = converter.convert_to(val_lit, 'liter', 'quart_impireal')
    print(f"   {val_lit} liter -> {quart_impireal_res:.4f} quart_impireal")

    # Using convert (Generic wrapper for convenience)
    
    val_cup_us = 10.5625 
    gallon_result = converter.convert(val_cup_us, 'cup_us', 'gallon_us')
    print(f"   {val_cup_us} cup_us -> {gallon_result:.4f} gallon_us")

    # Verification of accuracy with known constants
    
    expected_gal_to_liter = 3.785411784 * 2.0
    actual_gal_to_liter = converter.convert(2.0, 'gallon_us', 'liter')
    
    print("\n--- Accuracy Check ---")
    print(f"   Expected {expected_gal_to_liter:.6f} liter from 2 gallons.")
    print(f"   Calculated: {actual_gal_to_liter}")