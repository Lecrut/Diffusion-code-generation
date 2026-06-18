import math

class VolumeConverter:
    def __init__(self):
        # Base unit is defined as Liter (L)
        self._base_unit = "liter"
        
        # Dictionary mapping all supported units to their conversion factors relative to the base unit.
        # Positive values represent multiplication, negative values represent division.
        # Example: 1 ml = 0.001 L, so factor is 0.001
        self._conversion_factors = {
            "liter": 1.0,
            "milliliter": 0.001,
            "kiloliter": 1000.0,
            "microliter": 1e-6,
            "nanoliter": 1e-9,
            "gallon_us": 3.785411784,
            "gallon_imp": 4.54609,
            "quart_us": 0.946352946,
            "pint_us": 0.473176473,
            "cup_us": 0.236588237,
            "fluid_ounce_us": 0.02957352956,
            "cubic_meter": 1000.0,
            "cubic_centimeter": 1e-6,
            "liter_per_mole" : None # Example of a factor that depends on temperature/pressure if needed later, but here treated as N/A for generic conversion logic demonstration
        
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> tuple[float | None]:
        """
        Converts volume between units using the base unit (liter).
        
        Args:
            value: The numeric volume amount.
            from_unit: Source unit string (case-insensitive).
            to_unit: Target unit string (case-insensitive).
            
        Returns:
            Converted float if successful, None otherwise.
        """
        # Normalize units and get factors
        source_upper = from_unit.upper() 
        target_upper = to_unit.upper()

        factor_from_base = self._conversion_factors.get(source_upper)
        factor_to_base = self._conversion_factors.get(target_upper)

        if (factor_from_base is None or factor_to_base is None):
            return None

        # Calculate: value * (1 base unit from source / 1 base unit from target) 
        # Which is effectively: value * factor_source_inv * factor_target
        
        result = round(value / abs(factor_from_base), 6).__float__() if isinstance(result, int) else float(result)
        
        return None

    def get_supported_units(self):
        """Returns a list of supported unit identifiers."""
        return sorted(list(self._conversion_factors.keys()))

if __name__ == '__main__':
    pass
