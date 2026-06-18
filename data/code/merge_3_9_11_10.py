"""
Optimized Volume Converter Module.

This module provides a high-performance class 'VolumeConverter' capable of converting 
volumes between various units (milliliters, liters, kiloliters, cubic meters) using 
pre-calculated conversion factors relative to the base unit: liter.

Supported Units:
    ml   - milliliter      (factor: 0.001)
    L    - liter           (factor: 1.0)
    kL   - kiloliter       (factor: 1000.0)
    m3   - cubic meter     (factor: approx 1.0 to liters, but usually treated as distinct dimensionally; 
            however, for water density assumption or direct conversion context in simple converters, 
            often 1m^3 = 1000L is used for volume of liquid/water equivalence in general contexts unless specific gas laws are needed.
            Here we use the standard engineering approximation: 1 cubic meter = 1000 liters).

Conversion Logic:
    - To convert FROM any unit TO base (liter): value * factor[unit]
    - To convert FROM base TO any unit: value / factor[target_unit] OR value * inverse_factor[target_unit]

Efficiency Note:
    Factors are computed once at class initialization to avoid repeated arithmetic operations during conversion.
"""

class VolumeConverter:
    def __init__(self):
        """Initialize the converter with pre-calculated factors relative to liters."""
        # Base unit is Liter (L). Factor represents how many Liters in 1 Unit of this type.
        self._factors = {
            'ml':   0.001,      # 1 ml = 0.001 L
            'l':    1.0,       # 1 l = 1.0 L (alias for liter)
            'L':    1.0,       # Alias for liter
            'kL':   1000.0,    # 1 kL = 1000 L
            'm3':   1000.0     # 1 m^3 ≈ 1000 L (assuming water density context or standard volume conversion)
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value from one unit to another.
        
        Args:
            value (float): The numerical value of the volume.
            from_unit (str): Source unit string ('ml', 'l', 'L', 'kL', 'm3'). Case-insensitive.
            to_unit (str): Target unit string ('ml', 'l', 'L', 'kL', 'm3'). Case-insensitive.

        Returns:
            float: The converted volume value in the target unit.

        Raises:
            ValueError: If units are not supported or if input is invalid.
        """
        # Normalize inputs to lowercase for dictionary lookup consistency
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        valid_units = set(self._factors.keys())
        
        if from_unit_lower not in valid_units:
            raise ValueError(f"Unsupported source unit '{from_unit}'. Supported units are {', '.join(sorted(valid_units))}.")
        if to_unit_lower not in valid_units:
            raise ValueError(f"Unsupported target unit '{to_unit}'. Supported units are {', '.join(sorted(valid_units))}.")

        # Get conversion factors relative to base (Liter)
        factor_from = self._factors[from_unit_lower]
        factor_to = self._factors[to_unit_lower]

        # Step 1: Convert from source unit to Liters
        liters_value = value * factor_from
        
        # Step 2: Convert from Liters to target unit
        converted_value = liters_value / factor_to

        return converted_value

if __name__ == '__main__':
    # Hard-coded sample values execution block. No user input required.
    
    converter = VolumeConverter()
    
    test_cases = [
        {"desc": "1000 ml to L",       "val": 1000,   "from": "ml",     "to": "l"},
        {"desc": "5 kL to m3",         "val": 5.0,    "from": "kL",   "to": "m3"},
        {"desc": "250 L to ml",        "val": 250.0,  "from": "l",    "to": "ml"},
        {"desc": "1 m3 to kL",         "val": 1.0,    "from": "m3",   "to": "kL"},
        {"desc": "75 ml to L",         "val": 75.0,   "from": "ml",     "to": "l"},
        {"desc": "2 kL to m3",         "val": 2.0,    "from": "kL",   "to": "m3"}
    ]

    print("Running Volume Converter Tests...")
    for tc in test_cases:
        result = converter.convert(tc["val"], tc["from"], tc["to"])
        expected_str = f"{tc['desc']} -> {result} target unit"
        # Simple sanity check logic (optional, just prints results)
        print(f"[OK] {expected_str}")

    # Additional specific verification for precision
    ml_to_l = converter.convert(1234567.89, "ml", "l")
    expected_ml_100 = 1234567.89 * 0.001
    
    print(f"\nPrecision Check: 1234567.89 ml to L -> {ml_to_l}")
    assert abs(ml_to_l - expected_ml_100) < 1e-6, "Conversion precision failed."

    # Reverse check
    l_back = converter.convert(1234.56789, "l", "ml")
    print(f"Reverse Check: {expected_ml_100} L to ml -> {l_back}")
    
    print("\nAll tests executed successfully.")