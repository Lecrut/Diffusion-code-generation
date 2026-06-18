import math
from typing import Union, Optional

class UnitConverter:
    """Handles length unit conversions."""

    # Supported units and their conversion factors to meters (base unit)
    UNIT_FACTORS = {
        'm': 1.0,          # meter
        'km': 1000.0,      # kilometer
        'cm': 0.01,        # centimeter
        'mm': 0.001,       # millimeter
        'mi': 1609.344,    # mile (international)
        'yd': 0.9144,      # yard
        'ft': 0.3048,      # foot
        'in': 0.0254,      # inch
        'nm': 1e-9,        # nanometer
    }

    def __init__(self):
        """Initialize the converter with empty state."""
        pass

    @staticmethod
    def _validate_unit(unit: str) -> None:
        """Validate if a unit is supported. Raises ValueError if not."""
        lower_unit = unit.lower()
        if lower_unit not in UnitConverter.UNIT_FACTORS:
            raise ValueError(f"Unsupported length unit '{unit}'. Supported units are: {', '.join(UnitConverter.UNIT_FACTORS.keys())}")

    @staticmethod
    def _get_factor(unit: str) -> float:
        """Get the conversion factor for a given unit relative to meters."""
        UnitConverter._validate_unit(unit)
        return UnitConverter.UNIT_FACTORS[unit.lower()]

    def convert(self, length_value: Union[int, float], source_unit: str, target_unit: str) -> Union[float, int]:
        """
        Convert a length from one unit to another.

        Args:
            length_value (int | float): The value of the length in the source unit.
            source_unit (str): The starting unit of measurement.
            target_unit (str): The ending unit of measurement.

        Returns:
            Union[float, int]: The converted length in the target unit.
                               If result is a whole number and input was integer-like, returns int. Otherwise float.

        Raises:
            ValueError: If source or target units are not supported.
            TypeError: If inputs are of incorrect types.
        """
        if not isinstance(length_value, (int, float)):
            raise TypeError("Length value must be a number.")

        try:
            # Convert to base unit (meters) first
            meters = length_value * UnitConverter._get_factor(source_unit)
            
            # Then convert from meters to target unit
            result_meters = meters / UnitConverter._get_factor(target_unit)
            
            return int(result_meters) if isinstance(length_value, int) and math.isclose(int(result_meters), result_meters, rel_tol=1e-9) else float(result_meters)

        except ValueError as e:
            raise e

if __name__ == '__main__':
    # Hard-coded sample values for testing
    
    converter = UnitConverter()
    
    # Sample 1: Convert miles to kilometers
    result_1 = converter.convert(2, 'mi', 'km')
    print(f"Converted {result_1} km")

    # Sample 2: Convert feet to inches (expecting integer)
    result_2 = converter.convert(5.0, 'ft', 'in')
    print(f"Converted {result_2} in")

    # Sample 3: Invalid unit handling test (commented out as it raises exception)
    # try:
    #     converter.convert(10, 'miles_to_km', 'km')
    # except ValueError as e:
    #     print(f"Error caught: {e}")

    # Sample 4: Nanometers to meters (very small number)
    result_3 = converter.convert(500000000, 'nm', 'm')
    print(f"Converted {result_3} m")