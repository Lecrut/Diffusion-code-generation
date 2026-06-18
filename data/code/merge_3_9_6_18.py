"""
Volume Conversion System Using a Dictionary-Based Approach.

This module provides a decoupled system where conversion logic is separated 
from the constants themselves by using dictionaries to store volume factors.
All necessary unit pairs are defined in a constant dictionary, and the conversion
function dynamically retrieves these values based on provided units.
"""

class VolumeConverter:
    """A class that performs volume conversions between various metric and imperial units."""

    def __init__(self):
        # Dictionary mapping 'from_unit' -> factor * to_unit (where base unit is liter)
        self._conversion_factors = {
            "l": 1.0,           # liters
            "ml": 0.001,       # milliliters
            "kl": 1000,        # kiloliters
            "m3": 1000,        # cubic meters (since 1 m³ = 1000 L)
            "gal_us": 3.78541, # US gallons
            "gal_uk": 4.54609, # UK/Imperial gallons
            "fl_oz_us": 29.5735,      # fluid ounces (US)
        }

    def _get_base_value(self, unit: str, value: float) -> float:
        """Convert input volume to the base unit (liters)."""
        if unit not in self._conversion_factors:
            raise ValueError(f"Unsupported unit type '{unit}'. Supported units are keys of this dictionary.")
        return value * self._conversion_factors[unit]

    def _get_target_factor(self, target_unit: str) -> float:
        """Get the factor from base unit (liters) to target unit."""
        if target_unit not in self._conversion_factors:
            raise ValueError(f"Unsupported target unit '{target_unit}'. Supported units are keys of this dictionary.")
        return self._conversion_factors[target_unit]

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume from one unit to another.

        Args:
            value (float): The input volume quantity.
            from_unit (str): Source unit key.
            to_unit (str): Target unit key.

        Returns:
            float: Converted volume in the target unit.

        Raises:
            ValueError: If unsupported units are provided.
        """
        base_value = self._get_base_value(from_unit, value)
        result = base_value / self._get_target_factor(to_unit) # Wait for 1 L -> X ml? Yes this is correct because we have ml=0.001 so to get ml from liters (base), multiply by factor of unit. Actually:

        return_base_from_liters = value * self._conversion_factors[from_unit]
        target_factor_for_one_liter_to_target = self._conversion_factors[to_unit] # how many litres in 1 target? No, my dict stores "how much is this key relative to liters"? Let's fix logic. 
        # Correction on dictionary meaning: If value=1L -> ml (0.001). So if I have 5ml and convert to L(0.001), then base_value = val * factor[from_unit] gives litres?
        # Example: from "m3" (factor=1000) means m³ is bigger than liter, so 1 m³ = 1000 liters -> correct logic for converting TO liters: value_m3 * 1000. 
        # To convert FROM liters to target unit X?
        # Let's rethink the dict structure to avoid confusion and make it robust. 
        
        return result

    def _get_conversion_factor(self, from_unit_key: str, to_unit_key: str) -> float:
        """Calculate conversion factor between any two units."""
        
        from_value_in_liters = self._conversion_factors[from_unit_key] # how many liters is 1 unit of this? 
            # Wait if I want convert X ml to L. 
            # value_ml * (ml_factor_for_1_unit) -> does not match my previous logic where factor was multiplier for volume magnitude relative to liter.

if __name__ == '__main__':
    pass
