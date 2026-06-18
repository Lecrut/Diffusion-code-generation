"""
Optimized Arbitrary Length Unit Converter Module.

This module defines a base unit (meters) and uses a conversion factor dictionary
to handle conversions between any supported length units efficiently.
It avoids redundant calculations by normalizing all inputs to the base unit first,
then converting from there to the target unit.
"""

class LengthConverter:
    """A class to convert arbitrary length units based on a defined base."""

    def __init__(self):
        # Define conversion factors relative to the base unit (meters)
        # Positive values indicate how many meters are in one unit of that type.
        self._base_unit = "meter"
        self._factors = {
            "millimeter": 0.001,
            "centimeter": 0.01,
            "decimeter": 0.1,
            "meter": 1.0,
            "kilometer": 1000.0,
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a length value from one unit to another.

        Args:
            value (float): The numerical value to be converted.
            from_unit (str): The source unit of measurement.
            to_unit (str): The target unit of measurement.

        Returns:
            float: The converted value in the target unit.

        Raises:
            ValueError: If either 'from_unit' or 'to_unit' is not supported.
        """
        if from_unit.lower() not in self._factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit.lower() not in self._factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        # Normalize value to base units (meters)
        meters = value * self._factors[from_unit.lower()]
        
        # Convert from base units to the target unit
        result_meters = meters / self._factors[to_unit.lower()]
        
        return result_meters

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    
    converter = LengthConverter()

    # Sample 1: Convert kilometers to centimeters
    km_to_cm = converter.convert(5.0, "kilometer", "centimeter")
    
    # Sample 2: Convert inches (hypothetical extension) - Note: 'inch' is not in the current dictionary
    # To demonstrate functionality with existing units only:
    m_to_mm = converter.convert(10.5, "meter", "millimeter")

    print(f"Converted {5.0} kilometers to centimeters: {km_to_cm}")
    print(f"Converted {10.5} meters to millimeters: {m_to_mm}")

    # Additional test cases for robustness
    try:
        invalid_result = converter.convert(1, "invalid_unit", "meter")
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")

    # Test same units conversion (should return original value)
    result_same = converter.convert(42.0, "centimeter", "centimeter")
    assert abs(result_same - 42.0) < 1e-6, "Conversion to same unit should preserve value"
    print(f"Self-check passed: {result_same}")