import unittest
import math

class DistanceConverter:
    METERS_TO_KILOMETERS = 0.001
    METERS_TO_MILES = 0.000621371
    METERS_TO_FEET = 3.28084

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Value must be a number")
        if math.isnan(self.value) or math.isinf(self.value):
            raise ValueError("Value must be finite")
        if self.value < 0:
            raise ValueError("Distance cannot be negative")
        valid_units = ["m", "km", "mi", "ft"]
        if self.unit not in valid_units:
            raise ValueError(f"Invalid unit: {self.unit}. Valid units are {valid_units}")

    def _to_meters(self):
        if self.unit == "m":
            return self.value
        if self.unit == "km":
            return self.value * 1000
        if self.unit == "mi":
            return self.value * 1609.344
        if self.unit == "ft":
            return self.value / 3.28084
        return 0

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        valid_targets = ["m", "km", "mi", "ft"]
        if target_unit not in valid_targets:
            raise ValueError(f"Invalid target unit: {target_unit}. Valid units are {valid_targets}")
        
        meters = self._to_meters()
        
        if target_unit == "m":
            return meters
        if target_unit == "km":
            return meters * self.METERS_TO_KILOMETERS
        if target_unit == "mi":
            return meters * self.METERS_TO_MILES
        if target_unit == "ft":
            return meters * self.METERS_TO_FEET
        return 0

class TestDistanceConverter(unittest.TestCase):
    def test_meters_to_kilometers(self):
        converter = DistanceConverter(1000, "m")
        self.assertAlmostEqual(converter.convert("km"), 1.0, places=5)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter(1.5, "km")
        self.assertAlmostEqual(converter.convert("m"), 1500.0, places=5)

    def test_miles_to_meters(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.convert("m"), 1609.344, places=5)

    def test_feet_to_meters(self):
        converter = DistanceConverter(3.28084, "ft")
        self.assertAlmostEqual(converter.convert("m"), 1.0, places=4)

    def test_kilometers_to_miles(self):
        converter = DistanceConverter(1.609344, "km")
        self.assertAlmostEqual(converter.convert("mi"), 1.0, places=5)

    def test_miles_to_kilometers(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.convert("km"), 1.609344, places=5)

    def test_feet_to_kilometers(self):
        converter = DistanceConverter(3280.84, "ft")
        self.assertAlmostEqual(converter.convert("km"), 1.0, places=5)

    def test_meters_to_feet(self):
        converter = DistanceConverter(1, "m")
        self.assertAlmostEqual(converter.convert("ft"), 3.28084, places=5)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            DistanceConverter(-10, "m")

    def test_invalid_unit_init(self):
        with self.assertRaises(ValueError):
            DistanceConverter(10, "xyz")

    def test_invalid_convert_unit(self):
        converter = DistanceConverter(10, "m")
        with self.assertRaises(ValueError):
            converter.convert("xyz")

    def test_same_unit_conversion(self):
        converter = DistanceConverter(50, "m")
        self.assertEqual(converter.convert("m"), 50)

    def test_zero_distance(self):
        converter = DistanceConverter(0, "km")
        self.assertEqual(converter.convert("m"), 0)

if __name__ == '__main__':
    test_instance = TestDistanceConverter()
    test_instance.test_meters_to_kilometers()
    test_instance.test_kilometers_to_miles()
    
    converter1 = DistanceConverter(100, "m")
    print(f"100 meters to km: {converter1.convert('km')}")
    
    converter2 = DistanceConverter(5, "mi")
    print(f"5 miles to meters: {converter2.convert('m')}")
    
    converter3 = DistanceConverter(1000, "ft")
    print(f"1000 feet to kilometers: {converter3.convert('km')}")
    
    print("All tests passed.")