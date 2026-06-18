import math

class VolumeConverter:
    """
    A dictionary-based system for mapping volume conversion factors.
    The logic is decoupled from specific constants by using a central lookup table.
    
    Supported units include: L, ml (milliliter), m3 (cubic meter), gal (US gallon).
    Conversion direction defaults to 'to_base', but can be overridden per operation.
    """

    def __init__(self):
        # Base unit chosen as cubic meters (m³) for scientific consistency in this implementation,
        # though liters are often more practical. All factors relate to 1 m³ = 1000 L = 352749 ml = 264.172 gal.
        
        self._factors_to_base = {
            'm3': 1.0,
            'L': 1000.0,           # 1 m³ = 1000 L
            'ml': 1_000_000.0,    # 1 m³ = 1,000,000 ml (since 1 L = 1000 ml)
            'gal': 264.172053        # Approximate US gallons per cubic meter
        }

    def _get_factor(self, unit: str, direction: str):
        """
        Retrieve the conversion factor relative to a specific base or target unit.
        
        Args:
            unit (str): The source volume unit string (e.g., 'L', 'm3').
            direction (str): Direction of conversion ('to_base' for standard lookups, 
                            others handled by symmetry).

        Returns:
            float: Conversion factor to multiply the input value.
        
        Raises:
            ValueError: If an unsupported unit is provided or if factors are missing.
        """
        # Normalize direction logic
        reverse_factors = {v: k for k, v in self._factors_to_base.items()}

        base_unit = 'm3'  # Internal reference point
        
        if direction == 'to_base':
            return self._get_factor_for_source(unit)
        
        else: 
            target_unit = unit.lower()
            
            source_unit = reverse_factors.get(target_unit, None)
            
            if not source_unit or base_unit is None:
                raise ValueError(f"Unsupported conversion direction for {target_unit}")

    def _get_factor_for_source(self, unit_str):
        """Helper to get factor directly from the primary dictionary."""
        return self._factors_to_base.get(unit_str.lower(), None)

class VolumeConverterSystem(VolumeConverter):
    
    # Override base class methods with a more robust implementation using direct lookup
    
    def convert_volume(self, value: float, source_unit: str, target_unit: str = 'm3') -> float:
        """
        Convert volume from one unit to another.

        Args:
            value (float): The numeric value of the volume.
            source_unit (str): Source unit string ('L', 'ml', 'm³', 'gal').
            target_unit (str): Target unit string, defaults to cubic meters.

        Returns:
            float: Converted volume in the specified target unit.
        
        Raises:
            ValueError: If units are unsupported or conversion is invalid.
        """
        source_lower = str(source_unit).lower()
        target_lower = str(target_unit).lower()

        # Validate inputs against supported set
        if not self._is_valid_input(value):
            raise TypeError(f"Invalid value type for volume: {type(value).__name__}")

        try:
            factor_to_base_m3 = float(self._factors_to_base[source_lower])
            
            # Convert to base (m³) first, then apply target unit's factor relative to m³
            if not self._is_valid_input(target_unit):
                raise ValueError(f"Target unit '{target_unit}' is invalid. Supported: {list(self._factors_to_base.keys())}")

        except KeyError as e:
            raise ValueError(f"Unsupported source unit: {e}. Available units are L, ml, m3, gal.") from None
        
        # Convert to base (m³) then apply target factor relative to base
        converted_value = value * float(factor_to_base_m3) / 1.0

        return self._factors_to_base[target_lower]

    def _is_valid_input(self, input_val):
        """Check if the provided argument is a valid numeric type."""
        try: 
            int(input_val) or float(input_val)
            return True
        except (ValueError, TypeError):
            return False

# Main execution block with hard-coded sample values to demonstrate functionality without user interaction.

if __name__ == '__main__':
    # Initialize the converter system
    volume_system = VolumeConverterSystem()

    print("=== Volume Conversion System Demo ===")
    
    test_cases = [
        {"value": 1, "source": 'L', "target": 'ml'},           # Expected: ~1000 ml
        {"value": 2.5, "source": 'm3', "target": 'gal'},      # Expected: ~660 gal (approx)
        {"value": 1_000_000, "source": 'ml', "target": 'L'},   # Expected: ~1 L
        {"value": 50, "source": 'gal', "target": 'm3'}         # Expected: ~0.2 m³ (approx)
    ]

    for case in test_cases:
        try:
            result = volume_system.convert_volume(
                value=case["value"], 
                source_unit=case["source"], 
                target_unit=case["target"]
            )
            
            print(f"\nConversion Test:")
            print(f"  Input: {case['value']} {case['source']}")
            print(f"  Output: {result:.6f} {case['target']}")

        except Exception as e:
            # Handle any unexpected errors gracefully for demonstration purposes.
            print(f"\nError during conversion of {case}: {e}")

    print("\n=== Demo Complete ===")