"""
Distance Unit Converter Module

This module provides functionality to convert distances between various units of measurement.
It supports meters, kilometers, centimeters, millimeters, miles, yards, feet, inches.
The system prioritizes clarity and includes robust error handling for invalid inputs.
No external libraries are required; all calculations use standard Python arithmetic.
"""

from typing import Union

class DistanceConverter:
    """A class to handle distance conversions between supported units."""

    # Conversion factors relative to meters (1 unit = factor meters)
    METRIC_FACTORS = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
    }

    # Imperial conversion factors relative to meters (1 unit = factor meters)
    IMPERIAL_FACTORS = {
        "miles": 1609.344,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
    }

    ALL_UNITS = list(METRIC_FACTORS.keys()) + list(IMPERIAL_FACTORS.keys())

    def __init__(self):
        """Initialize the DistanceConverter with empty state."""
        pass

    def convert(self, value: Union[int, float], from_unit: str, to_unit: str) -> dict[str, Union[float, int]]:
        """
        Convert a distance from one unit to another.

        Args:
            value (int or float): The numerical value of the distance.
            from_unit (str): Source unit string. Must be in ALL_UNITS.
            to_unit (str): Target unit string. Must be in ALL_UNITS.

        Returns:
            dict[str, Union[float, int]]: A dictionary containing 'original', 
                                        'converted_value', and 'target_unit'.
        
        Raises:
            ValueError: If from_unit or to_unit is not supported.
                       Or if the input value is invalid (non-numeric).
        """
        # Validate numeric type
        try:
            float(value)
        except TypeError:
            raise ValueError("Input distance must be a number.")

        normalized_value = float(value)

        # Check unit validity
        from_unit_lower = from_unit.lower() if isinstance(from_unit, str) else ""
        to_unit_lower = to_unit.lower() if isinstance(to_unit, str) else ""

        if not (from_unit_lower in self.ALL_UNITS and to_unit_lower in self.ALL_UNITS):
            raise ValueError(f"Unsupported unit(s). Supported units: {', '.join(self.ALL_UNITS)}")

        # Get conversion factors relative to meters
        factor_from = 0.0
        for key, val in self.METRIC_FACTORS.items():
            if from_unit_lower == key.lower():
                factor_from = val
                break
        
        for key, val in self.IMPERIAL_FACTORS.items():
            if from_unit_lower == key.lower():
                factor_from = val

        # Calculate value in meters first to avoid precision issues with mixed systems
        meters_value = normalized_value * factor_from

        target_factor = 0.0
        for key, val in self.METRIC_FACTORS.items():
            if to_unit_lower == key.lower():
                target_factor = val / meters_value # Wait, logic error below correction needed
                
                break
        
        for key, val in self.IMPERIAL_FACTORS.items():
            if to_unit_lower == key.lower():
                target_factor = 1.0 / (val) # This is wrong too. Let's rewrite calculation cleanly.

    def _get_meters_value(self, value: float, unit_str: str):
        """Helper to get meters equivalent."""
        u = unit_str.lower()
        if u in self.METRIC_FACTORS:
            return value * self.METRIC_FACTORS[u]
        elif u in self.IMPERIAL_FACTORS:
            return value * self.IMPERIAL_FACTORS[u]
        else:
            raise ValueError(f"Unknown unit: {unit_str}")

    def _get_unit_value(self, meters_val: float, target_unit_str: str):
        """Helper to get target unit from meters."""
        u = target_unit_str.lower()
        if u in self.METRIC_FACTORS:
            return meters_val / self.METRIC_FACTORS[u]
        elif u in self.IMPERIAL_FACTORS:
            return meters_val / self.IMPERIAL_FACTORS[u]
        else:
            raise ValueError(f"Unknown unit: {target_unit_str}")

    def convert(self, value: Union[int, float], from_unit: str, to_unit: str) -> dict[str, Union[float, int]]:
        """
        Convert a distance from one unit to another.

        Args:
            value (int or float): The numerical value of the distance.
            from_unit (str): Source unit string. Must be in ALL_UNITS.
            to_unit (str): Target unit string. Must be in ALL_UNITS.

        Returns:
            dict[str, Union[float, int]]: A dictionary containing 'original', 
                                        'converted_value', and 'target_unit'.
        
        Raises:
            ValueError: If from_unit or to_unit is not supported.
                       Or if the input value is invalid (non-numeric).
        """
        # Validate numeric type
        try:
            normalized_value = float(value)
        except TypeError:
            raise ValueError("Input distance must be a number.")

        # Check unit validity and get meters equivalent
        from_unit_lower = str(from_unit).lower()
        to_unit_lower = str(to_unit).lower()

        if not (from_unit_lower in self.ALL_UNITS and to_unit_lower in self.ALL_UNITS):
            raise ValueError(f"Unsupported unit(s). Supported units: {', '.join(self.ALL_UNITS)}")

        meters_value = self._get_meters_value(normalized_value, from_unit)
        
        # Round slightly for cleaner output if needed, but keep precision here
        converted_val = self._get_unit_value(meters_value, to_unit_lower)

        return {
            "original": normalized_value,
            "converted_value": round(converted_val, 6),
            "target_unit": str(to_unit).lower()
        }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI args
    
    converter = DistanceConverter()

    test_cases = [
        {"value": 10, "from_unit": "meters", "to_unit": "feet"},
        {"value": 5.5, "from_unit": "kilometers", "to_unit": "miles"},
        {"value": 2000, "from_unit": "inches", "to_unit": "yards"},
        {"value": -10, "from_unit": "feet", "to_unit": "centimeters"}, # Negative distance test
    ]

    print("Distance Conversion Results:")
    print("-" * 40)

    for tc in test_cases:
        try:
            result = converter.convert(tc["value"], tc["from_unit"], tc["to_unit"])
            original_val = str(result['original']) if isinstance(result['original'], float) else int(result['original'])
            
            print(f"Input: {tc['value']} {tc['from_unit'].capitalize()}")
            print(f"Output: {result['converted_value']:.4f} {result['target_unit']}")
            print("-" * 40)

        except ValueError as e:
            # Since we are using hard-coded valid inputs, this block demonstrates error handling capability.
            # In a real scenario with user input, 'e' would contain the specific error message.
            print(f"Error processing {tc}: {str(e)}")