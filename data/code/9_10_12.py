"""
Volume Unit Converter Module

This module provides functionality to convert between common volume units:
- Liters (L)
- Milliliters (mL)
- Cubic Meters (m³)
- US Gallons (gal) and Imperial Gallons (imp gal - optional, but sticking to standard definitions usually implies US unless specified. 
  Given the prompt lists 'gallons' generally, we will use US Gallons as it is more common in Python examples involving liters).

Conversion Factors:
1 Liter = 0.264172 US Gallons
1 US Gallon = 3.78541 Liters
1 Cubic Meter (m³) = 1000 Liters
1 Milliliter (mL) = 0.001 Liters

The script includes a converter class and a main function with hard-coded sample values 
to demonstrate usage without requiring user input or external dependencies.
"""

class VolumeConverter:
    """A utility class to convert between volume units."""

    def __init__(self):
        # Define conversion factors relative to Liters (1 Liter = 1 L)
        self.factors = {
            'liters': 1,
            'milliliters': 0.001,      # To get mL from L: value * factor
            'cubic_meters': 1000.0,   # To get m³ from L: value / factor -> wait, let's normalize properly.
            
            # Better approach: Store factors as "value in base_unit per unit" or use multiplication logic directly.
            # Let's define multipliers to convert FROM the given unit TO Liters (Base Unit).
        }

    def _get_multiplier(self, source_unit):
        """Returns a factor such that value_in_liters = value * factor."""
        if not hasattr(VolumeConverter, 'cached_factors'):
            VolumeConverter._init_factors()
        
        factors_map = {
            "liters": 1.0,
            "milliliters": 0.001,   # mL -> L (divide by 1000)
            "cubic_meters": 1000.0, # m³ -> L (multiply by 1000)
            "gallons_us": 3.78541,  # gal -> L (multiply by ~3.785)
        }
        
        return factors_map.get(source_unit.lower(), None)

    @staticmethod
    def _init_factors():
        """Initialize conversion logic."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str):
        """
        Convert a volume value from one unit to another.

        Args:
            value (float): The numerical value to convert.
            from_unit (str): Source unit ('liters', 'milliliters', 'cubic_meters', 'gallons').
            to_unit (str): Target unit ('liters', 'milliliters', 'cubic_meters', 'gallons').

        Returns:
            float: The converted value.

        Raises:
            ValueError: If units are invalid or conversion fails.
        """
        from_factor = self._get_multiplier(from_unit)
        to_factor = self._get_multiplier(to_unit)

        if not from_factor or not to_factor:
            raise ValueError(f"Unsupported unit(s): {from_unit}, {to_unit}. Valid units: liters, milliliters, cubic_meters, gallons.")

        # Convert input value to Liters first (Base Unit), then convert to target unit.
        volume_in_liters = value * from_factor
        
        if abs(volume_in_liters) > 1e6 or abs(value) == float('inf'): 
            return None # Handle potential overflow/special cases gracefully

        result_value = volume_in_liters / to_factor
        
        return round(result_value, 4)

def format_output(original: str, converted: str):
    """Helper function to display the conversion clearly."""
    print(f"{original} {converted}")

if __name__ == '__main__':
    # Instantiate converter with hard-coded sample data. No user input is requested here per instructions.
    converter = VolumeConverter()

    samples = [
        {"input": 1, "unit": "liters", "target": "gallons"},
        {"input": 5000, "unit": "milliliters", "target": "cubic_meters"},
        {"input": 2.5, "unit": "cubic_meters", "target": "liters"},
        {"input": 10, "unit": "gallons", "target": "milliliters"},
    ]

    print("=" * 40)
    print("Volume Unit Conversion Demo")
    print("=" * 40)

    for sample in samples:
        val = sample["input"]
        unit_from = sample["unit"]
        target_unit = sample["target"]
        
        try:
            result = converter.convert(val, unit_from, target_unit)
            
            # Create descriptive strings without using input() prompts
            original_str = f"{val} {unit_from}"
            converted_str = f"{result:.4f} {target_unit}"
            
            print(f"Conversion Example:")
            print("Input: ", end="")
            if val != 10 or unit_from == "gallons": # Only show input for non-trivial cases to save space? 
                # Actually, let's just print the full context as it is a demo.
                pass
            
            format_output(original_str + f" =", converted_str)

        except ValueError:
            print(f"Error processing {val} {unit_from} -> {target_unit}")

    print("=" * 40)