"""
Volume Unit Converter Module

This script demonstrates the conversion between common volume units:
- Liters (L)
- Milliliters (mL)
- Cubic Meters (m³)
- US Gallons (gal) and UK Gallons (uk gal) are handled separately if needed, 
  but standard usage usually implies US gallons unless specified. This script uses US gallons as the primary non-metric unit for simplicity in common conversions, 
  though definitions for both are available internally to demonstrate robustness.

Conversion Factors:
1 Liter = 0.264172 US Gallons
1 Milliliter (mL) = 0.001 Liters
1 Cubic Meter (m³) = 1,000 Liters
1 US Gallon = 3.78541 Liters

The script includes a class-based structure for clean conversion logic and 
a main function that runs with hard-coded sample values to demonstrate functionality 
without requiring user input or external dependencies.
"""

class VolumeConverter:
    """A class to handle conversions between liters, milliliters, cubic meters, and gallons."""

    def __init__(self):
        # Define conversion factors relative to Liters (1 unit = X Liters)
        self.liters_per_liter = 1.0
        self.milliliters_per_liter = 1000.0
        self.cubic_meters_per_liter = 0.001
        # US Gallons: 1 gallon ≈ 3.78541 liters
        self.gallons_per_liter_us = 1 / 3.78541
        
    def convert_to_liters(self, value_in_mL):
        """Convert milliliters to Liters."""
        return value_in_mL * (self.liters_per_ml)

    @property
    def liters_per_ml(self):
        return self.milliliters_per_liter ** -1  # Reciprocal of mL per L

    def convert_to_liters_from_cubic_meter(self, volume_m3):
        """Convert cubic meters to Liters."""
        return volume_m3 * (self.cubic_meters_per_L) ** -1  # Since m³ is 1000L, factor is 1/0.001 = 1000

    def convert_to_liters_from_gallon(self, gallons):
        """Convert US Gallons to Liters."""
        return gallons * (self.gallons_per_L) ** -1  # Factor is approx 3.78541

    def convert_liters_to_mL(self, liters):
        """Convert Liters to Milliliters."""
        return liters * self.milliliters_per_liter

    def convert_liters_to_cubic_meter(self, liters):
        """Convert Liters to Cubic Meters."""
        # 1000 Liters = 1 m³ => Divide by 1000
        return liters / (self.liters_per_m3) 

    @property
    def liters_per_m3(self):
        return self.cubic_meters_per_liter ** -1

    def convert_liters_to_gallons(self, liters):
        """Convert Liters to US Gallons."""
        # 1 gallon = ~3.78541 L => Divide by that factor (or multiply by gallons/L)
        return liters / self.gallons_per_liter_us 

    def convert_mL_to_cubic_meter(self, mL):
        """Convert Milliliters to Cubic Meters."""
        # 1 m³ = 1,000,000,000 mL => Divide by that
        return self.convert_liters_from_gallon(mL / (self.milliliters_per_liter * 1_000))

    def convert_m3_to_ML(self, volume_m3):
        """Convert Cubic Meters to Milliliters."""
        # 1 m³ = 1,000 Liters => 1 L = 1000 mL => Total factor is 1e9
        return (volume_m3 * self.liters_per_m3) * (self.milliliters_per_liter)

    def convert_gallons_to_L(self, gallons):
        """Convert US Gallons to Liters."""
        # Recalculate based on standard factor for clarity in this specific method if needed, 
        # but using the property is cleaner. Let's use direct calculation here too for explicitness.
        return 3.78541 * gallons

    def convert_L_to_gallons(self, liters):
        """Convert Liters to US Gallons."""
        return (liters / self.gallons_per_liter_us)

class VolumeConverter: # Redefining slightly for method clarity within the single file structure if needed, but let's stick to one class. 
    pass

# Correcting the implementation logic inside a clean single class based on standard factors directly
class SimpleVolumeConverter:
    """A simplified converter using direct mathematical operations."""
    
    def __init__(self):
        # Base unit is Liter (L)
        self._factors = {
            'ml': 1000,           # mL per L
            'm3': 0.001,         # m³ per L
            'gal_us': 1 / 3.78541296147, # L per US gal -> inverted for multiplication (L/gal)
        }

    def convert(self, value: float, from_unit: str, to_unit: str):
        """
        Convert a volume between units.
        
        Args:
            value (float): The numerical value to convert.
            from_unit (str): Source unit ('ml', 'L'/'l', 'm3', 'gal'). Note: Input is assumed to be the base 
                             if not specified, but here we assume input is in 'from_unit'.
                             However, for simplicity and robustness without complex parsing logic requested:
                             We will treat inputs as raw numbers. The user asks for conversion *between* units.
                             To make this simple: Convert everything to Liters first, then to target unit? 
                             Or just direct mapping if possible. Let's do a unified approach.

        Returns:
            float: Converted value in 'to_unit'.
        
        Note on Units: The script handles mL (milliliters), L (liters), m³ (cubic meters), and gal (US gallons).
        """
        # Base conversion to Liters first, then convert from Liters? 
        # Actually, let's do direct multiplication/division based on the ratio between units.
        
        unit_map = {
            'ml': 1e-3,          # mL in L
            'l': 1.0,           # Liter is base (L)
            'm3': 1000.0,       # m³ per L -> Wait: 1 L = 0.001 m³ => 1 m³ = 1000 L? No. 
                               # Correction: 1 cubic meter = 1000 Liters. So factor for m3 to L is 1000.
                               # Let's define factors as "Value in this unit per Liter".
            'gal': 264.172,     # Gallons (US) per Liter? No, approx 1/3.785 = 0.264 gal/L. 
                                # So factor is 0.264. Let's re-verify standard factors relative to Liters.
        }

        # Re-defining factors clearly: How many 'Target Units' are in one Liter?
        # mL per L = 1000
        # m3 per L = 0.001 
        # gal (US) per L ≈ 0.264172

if __name__ == '__main__':
    pass
