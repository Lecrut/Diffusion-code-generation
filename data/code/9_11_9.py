import math

class VolumeConverter:
    """A high-efficiency class to convert between various volume units."""

    # Conversion factors relative to Liters (base unit)
    FACTORS = {
        'litre': 1.0,           # Base unit
        'millilitre': 0.001,   # 1 mL = 0.001 L
        'kilolitre': 1000.0,   # 1 kL = 1000 L
        'gallon_us': 3.785411784,  # US fluid gallon to Liters (inverse: factor for input) -> Actually defined as Liter/Unit or Unit/Liter?
                                 # Let's define FACTORS[unit] such that Value_Unit * FACTOR = Value_Liters.
        'quart_us': 0.946352946,   # US quart to Liters
        'pint_us': 0.473176473,    # US pint to Liters
        'cup_us': 0.236588237,     # US cup to Liters
        'gallon_imp': 4.54609,      # Imperial gallon to Liters
        'quart_imp': 1.1365225,    # Imperial quart to Liters
        'pint_imp': 0.56826125,     # Imperial pint to Litars (typo fixed above thought) -> pints are often confused with imperial and us cups? No, let's stick to clear definitions.
                                    # Wait, my previous line "Imperial quart" was correct but factor logic needs verification relative to liters.
        'pint_uk': 0.56826125,    # UK pint to Liters (same as 4 * Imperial Quart / 7? No. 1 gal = 8 pints). 
                                   # Actually: 1 Imp Gal = 4.54609 L -> 1 imp Pint = 4.54609/8 = 0.56826...
        'tablespoon_us': 0.014786764, # US tbsp to Liters
    }

    def __init__(self):
        self._base_unit = "litre"

    @classmethod
    def get_supported_units(cls) -> list:
        """Return a sorted list of supported volume units."""
        return sorted(FACTORS.keys())

    def convert_to_base(self, value: float | int, from_unit: str) -> float:
        """
        Convert a given quantity to the base unit (liters).
        
        Args:
            value: The numerical value in 'from_unit'.
            from_unit: The source volume unit string.

        Returns:
            The converted value in liters.
            
        Raises:
            ValueError: If 'from_unit' is not supported or if input is invalid.
        """
        factor = FACTORS.get(from_unit)
        if factor is None:
            raise ValueError(f"Unsupported unit '{from_unit}'. Supported units are {self.get_supported_units()}")
        return value * factor

    def convert_from_base(self, volume_liters: float | int, to_unit: str) -> float:
        """
        Convert a given quantity from the base unit (liters) to another supported unit.

        Args:
            volume_liters: The numerical value in liters.
            to_unit: The target volume unit string.

        Returns:
            The converted value in 'to_unit'.
            
        Raises:
            ValueError: If 'to_unit' is not supported or if input is invalid.
        """
        factor_target = FACTORS.get(to_unit)
        # To convert Liters -> Target Unit, we need the inverse of Factor(Target).
        # Value_Target = Volume_Liters / (Liters_per_Target_Unit_factor in my dict? No.)
        # My definition: VALUE_UNITS * FACTOR_TO_LITERS = LITERS.
        # Therefore: VALUE_TARGETS = LITERS / FACTOR_TO_LITERS
        
        if factor_target is None:
            raise ValueError(f"Unsupported unit '{to_unit}'. Supported units are {self.get_supported_units()}")

if __name__ == '__main__':
    pass
