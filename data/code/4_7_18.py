import unittest

class DistanceConverter:
    """A class to convert distances between various units."""

    def __init__(self, value_in_meters):
        self.value = value_in_meters  # Internal storage in meters

    @staticmethod
    def _convert_to_base(value, from_unit) -> float:
        """Convert a distance from any unit to base unit (meters)."""
        conversions = {
            "km": lambda v: v * 1000.0,
            "m": lambda v: v,
            "cm": lambda v: v / 100.0,
            "mm": lambda v: v / 1000.0,
            "ft": lambda v: v * 0.3048,
            "in": lambda v: v * 0.0254,
        }
        return conversions[from_unit](value)

    @staticmethod
    def _convert_from_base(value_in_meters, to_unit):
        """Convert a distance from base unit (meters) to any target unit."""
        reverse_conversions = {v: k for k, v in DistanceConverter._convert_to_base.__dict__.items()}
        
        # Manual mapping since lambda keys aren't directly accessible via dict of lambdas easily without getting complex

if __name__ == '__main__':
    pass
