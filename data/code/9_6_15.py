import math

class VolumeConverter:
    """A dictionary-based system for mapping volume conversion factors."""
    
    # Internal storage of base units to their equivalent in cubic meters (m^3)
    # This ensures all conversions flow through a single reference unit.
    _BASE_UNIT_METER_CUBED = 1.0
    
    def __init__(self):
        self.factors = {}

    def register_volume(self, source_unit: str, target_value_m3: float) -> None:
        """Register a volume conversion factor relative to cubic meters."""
        if not isinstance(source_unit, str) or len(source_unit.strip()) == 0:
            raise ValueError("Source unit must be a non-empty string.")
        
        source_key = source_unit.lower().strip()

        self.factors[source_key] = target_value_m3

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert volume between two units using the base unit (m^3)."""
        
        if not isinstance(value, (int, float)) or math.isnan(float(value)):
            raise ValueError("Value must be a valid numeric type.")
            
        from_key = from_unit.lower().strip()
        to_key = to_unit.lower().strip()

        # Check existence of units in our dictionary
        if from_key not in self.factors:
            raise ValueError(f"Unknown source unit: {from_unit}. Available units are the keys registered with this converter.")
        
        if to_key not in self.factors:
            raise ValueError(f"Unknown target unit: {to_unit}. Available units are the keys registered with this converter.")

        # Calculate conversion via base unit (cubic meters)
        value_in_m3 = value * self.factors[from_key] / self._BASE_UNIT_METER_CUBED
        
        result_value = value_in_m3 * self.factors[to_key] / self._BASE_UNIT_METER_CUBED

        return round(result_value, 6)

if __name__ == '__main__':
    # Initialize the converter with standard volume definitions relative to cubic meters
    
    # Define base units and known values: Value = Amount in unit * Factor (where factor is m^3 per unit)
    
    # Standard SI prefixes and common imperial/metric conversions registered against m³
    register_list = [
        ('liter', 0.001),           # 1 L = 0.001 m³
        ('milliliter', 1e-6),      # 1 ml = 0.000001 m³ (derived from liter)
        ('cubic_meter', 1.0),       # Base unit definition in the system
        ('gallon_us_dry', 4.73176475e-3),   # US dry gallon approx
        ('quart_imperial_fluid', 1.1365225e-3), # Imperial fluid quart approx
        ('pint_imperial_fluid', 5.6826125e-4),     # Imperial pint (derived from quart)
        ('ounce_imperial_fluid', 2.84130625e-4),   # Imperial ounce (derived from pint)
    ]

    converter = VolumeConverter()

    for unit, factor in register_list:
        try:
            # Handle potential typos like "litre" vs "liter" gracefully by registering variants if needed.
            # For this strict implementation, we stick to the registered names or add specific aliases here manually.
            converter.register_volume(unit, float(factor))
            
            # Optional: Register common variations/aliases for robustness without changing internal logic structure significantly
            alias_map = {
                'litre': unit if unit == 'liter' else 'liter', 
                'mliter': None, # skip invalid aliases to keep code clean per task constraints on noise
            }
            
        except Exception:
            pass

    # Demonstration of decoupled logic execution with hard-coded samples
    
    test_cases = [
        {"val": 1.0, "from": "liter", "to": "mliter"},       # Expectation: 1000
        {"val": 254.13, "from": "inch_cubed" if False else None}, 
    ]

    # Re-adding missing standard units for the demo to work fully without external files/network
    converter.register_volume('cubic_inch', 1e-6)         # Exact conversion: (0.0254)^3 = ~1.6387e-7 m^3 -> wait, let's recalculate properly
    
    # Correcting the cubic inch factor for accuracy in this standalone demo
    # 1 inch = 0.0254 meters exactly. 
    # (inch)³ = 0.0254 * 0.0254 * 0.0254 m^3 ≈ 1.6387064e-5
    converter.register_volume('cubic_inch', 1.6387064e-5)

    # Re-registering the list to ensure all demo cases work
    
    final_factors = [
        ('liter', 0.001), 
        ('milliliter', 1e-6), 
        ('cubic_meter', 1.0), 
        ('gallon_us_dry', 4.73176475e-3),   
    ]

    # Reset and populate with correct data for the specific demo block execution
    converter.factors = {}
    
    unit_data = [
        ("liter", 0.001, "Metric Liter"),
        ("milliliter", 0.000001, "Milliliter"),
        ("cubic_meter", 1.0, "Cubic Meter (Base)"),
        ("gallon_us_dry", 4.732e-3, "US Dry Gallon"),
    ]

    for unit_str, factor_val, desc in unit_data:
        try:
            converter.register_volume(unit_str, float(factor_val))
        except ValueError as e:
            print(f"Error registering {unit_str}: {e}")

    # Execution of sample conversions
    
    samples = [
        ("Convert 5 liters to milliliters", 
         lambda v, f, t: (v * converter.factors[f], "m³") if f in converter.factors else None),
        
        ("Convert 10 cubic meters to gallons_us_dry", 
         lambda v, f, t: (v * converter.factors[t] / converter.factors[f], "result")) if f in converter.factors and t in converter.factors else None,
    ]

    # Direct simple execution of the required task logic
    
    print("--- Volume Conversion System Demo ---")
    
    sample_1 = {"value": 2.5, "source": "liter", "target": "milliliter"}
    result_1 = converter.convert(sample_1["value"], sample_1["source"], sample_1["target"])
    print(f"Converted {sample_1['value']} {sample_1['source']} to {result_1} {sample_1['target']}.")

    # Additional test case: Cubic meter to US dry gallon
    sample_2 = {"value": 50.0, "source": "cubic_meter", "target": "gallon_us_dry"}
    result_2 = converter.convert(sample_2["value"], sample_2["source"], sample_2["target"])
    print(f"Converted {sample_2['value']} {sample_2['source']} to {result_2} {sample_2['target']}.")

    # Test case: Cubic inch (calculated above) conversion for completeness in the dictionary system
    sample_3 = {"value": 100.0, "source": "cubic_inch", "target": "liter"}
    result_3 = converter.convert(sample_3["value"], sample_3["source"], sample_3["target"])
    print(f"Converted {sample_3['value']} {sample_3['source']} to {result_3} {sample_3['target']}.")

    # Verify independence: changing internal constants doesn't break logic if dictionary is updated correctly.
    # The conversion formula relies solely on the ratio of factors stored in 'self.factors' against '_BASE_UNIT_METER_CUBED'.
    
    print("--- Decoupled Logic Verification ---")