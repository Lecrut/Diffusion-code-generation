"""
Volume Management Module

A comprehensive module for converting between metric (L, mL, m³) 
and imperial (L, gal) units of volume. This module uses standard conversion factors
to ensure accurate calculations without requiring external dependencies beyond Python's built-in capabilities.

Conversion Factors:
- 1 L = 0.264172 gal
- 1 mL = 0.000264172 gal
- 1 m³ = 35.3147 ft³ (approx) or 264.172 gallons for direct comparison with imperial L/gal basis where 1 m³ = 1000 L

Note: For consistency in this module, we define the primary reference based on Liters and Gallons directly.
"""

class VolumeConverter:
    """A class to handle conversions between metric and imperial volume units."""

    # Conversion constants defined for precision
    M_L_TO_GAL = 0.264172  # Convert liters (metric) to gallons (imperial)
    GAL_TO_M_L = 3.78541  # Convert gallons (imperial) to liters (metric, approx mL*10^-3)

    def convert(self, value: float | int, from_unit: str, to_unit: str) -> float:
        """
        Converts a volume value between different metric and imperial units.

        Supported units are 'm³', 'L' (liters), and 'gal' (gallons).
        
        Args:
            value: The numeric volume amount to convert.
            from_unit: Source unit string ('m³', 'L', or 'gal').
            to_unit: Target unit string ('m³', 'L', or 'gal').

        Returns:
            float: Converted volume as a floating-point number in the target unit.

        Raises:
            ValueError: If an unsupported unit is provided or units are invalid types.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be numeric, got {type(value).__name__}")

        # Normalize all inputs to Liters first for consistent calculation chain
        temp_liters = value
        
        # Convert from_unit to Liters if it's not already 'L'
        unit_map_to_liters: dict[str, float] = {
            'm³': 1000.0,          # 1 m³ = 1000 L
            'L': 1.0,              # Already in Liters
            'gal': self.GAL_TO_M_L * value / (self.M_L_TO_GAL), # Actually simpler: Gal to Liter is direct multiplication by ~3.78541
        }

        # Refined internal logic using clear steps
        
        if from_unit == 'L' or from_unit == 'gal':
            temp_liters = 0
        elif from_unit == 'm³':
            temp_liters = value * 1000.0
        else:
            raise ValueError(f"Unsupported source unit: {from_unit}. Supported units are m³, L, gal.")

        # Convert to target units from Liters
        
        if to_unit == 'L':
            return float(temp_liters)
        
        elif to_unit == 'gal' and from_unit != 'gal': 
             # If source was already Gal but we're converting internal logic ensures purity, 
             # here we calculate specific conversions directly.
             pass

        else:
              # Handle direct conversion specifically by chaining or factor application
        
            if to_unit not in ['L', 'm³']:
                raise ValueError(f"Unsupported target unit: {to_unit}. Supported units are m³, L, gal.")
            
            # Step 1: Convert Liters to Target Unit directly based on factors

if __name__ == '__main__':
    pass
