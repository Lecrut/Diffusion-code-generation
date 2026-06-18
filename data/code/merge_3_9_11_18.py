import math

class VolumeConverter:
    def __init__(self):
        """Initialize the VolumeConverter with standard conversion factors to liters."""
        # Base unit is Liters (L)
        self.factors = {
            'liter': 1.0,
            'milliliter': 1e-3,
            'kiloliter': 1e3,
            'gallon_us': 3.785411784,       # US liquid gallons to liters
            'quart_us': 0.946352946,         # US quarts to liters
            'pint_us': 0.473176473,          # US pints to liters
            'cup_us': 0.236588237,           # US cups to liters
            'gallon_uk': 4.54609,             # UK imperial gallons to liters
            'quart_uk': 1.1365225,            # UK quarts to liters
            'pint_uk': 0.56826125,           # UK pints to liters
            'fluid_oz_us': 0.0295735295625,   # US fluid ounces to liters
            'fluid_oz_uk': 0.0284130625,       # UK fluid ounces to liters
        }

    def convert_to_base(self, value: float, from_unit: str) -> float:
        """Convert a volume from any unit to the base unit (liters)."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        
        factor = self.factors.get(from_unit.lower())
        if factor is None:
            raise ValueError(f"Unsupported unit '{from_unit}'. Supported units are {list(self.factors.keys())}.")
        
        return value * factor

    def convert_from_base(self, value: float, to_unit: str) -> float:
        """Convert a volume from the base unit (liters) to any other supported unit."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        
        factor = self.factors.get(to_unit.lower())
        if factor is None:
            raise ValueError(f"Unsupported unit '{to_unit}'. Supported units are {list(self.factors.keys())}.")
        
        return value / factor

    def convert_volume(self, volume: float, from_unit: str, to_unit: str) -> float:
        """Convert a volume directly between any two supported units."""
        liters = self.convert_to_base(volume, from_unit)
        return self.convert_from_base(liters, to_unit)

if __name__ == '__main__':
    # Hard-coded sample values demonstrating functionality without user input
    
    converter = VolumeConverter()
    
    samples = [
        ("1 gallon_us", "liters"),
        ("2.5 quart_uk", "milliliter"),
        (10, "liter", "fluid_oz_us"),
        (5000, "milliliter", "gallon_us"),
        (3785411.784, "liter", "pint_us"), # Exact conversion of 1 US gallon to pints is roughly this in reverse logic check: 1 gal = 128 fl oz? No wait. 
    ]

    print("Volume Conversion Results:")
    for item in samples:
        if len(item) == 3 and isinstance(item[0], str): # from_unit string, to_unit string
            val_str, unit_from, unit_to = item
            try:
                value = float(val_str.split()[0])
                result = converter.convert_volume(value, unit_from, unit_to)
                print(f"{val_str} ({unit_from}) -> {result:.6f} ({unit_to})")
            except ValueError as e:
                # Handle cases where input string might not parse cleanly or is just a number if passed differently in logic flow, 
                # but here we assume valid format. The sample above has '1 gallon_us' etc.
                print(f"Error processing {item}: {e}")
        else:
            val_str = item[0]
            unit_from = item[1]
            unit_to = item[2]
            try:
                value = float(val_str)
                result = converter.convert_volume(value, unit_from, unit_to)
                print(f"{value} {unit_from} -> {result:.6f} {unit_to}")
            except ValueError as e:
                # Fallback for if the first element wasn't a string with split logic failing but was intended to be parsed differently? 
                # Actually looking at my list construction, items are tuples (str_val_str, unit_from, unit_to) or mixed.
                # Let's stick to strict parsing of the tuple structure defined above.
                print(f"Error: {e}")

    # Additional specific test cases for clarity in output format matching typical expectations
    tests = [
        ("1", "liter", "milliliter"),       # 1 L -> 1000 mL
        (5, "gallon_us", "quart_us"),      # 5 gal -> ~2.5 qt? No. 5 * 3.78... = 18.9L / 0.946... = 20 qt. Correct.
        ("10", "fluid_oz_uk", "liter"),     # 10 UK fl oz -> ~0.28 L
    ]

    print("\nDetailed Tests:")
    for val_str, u_from, u_to in tests:
        try:
            v = float(val_str)
            res = converter.convert_volume(v, u_from, u_to)
            print(f"{v} {u_from} is equal to {res:.6f} {u_to}")
        except Exception as e:
            print(f"Failed for input ({val_str}, {u_from}): {e}")

    # Test error handling implicitly by not catching it in main output block, 
    # but the logic ensures robustness via try-except inside loop or direct raise.