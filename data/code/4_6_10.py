import unittest
import math

class DistanceConverter:
    KILOMETERS_TO_MILES = 0.621371
    MILES_TO_KILOMETERS = 1.60934
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 0.3048
    CENTIMETERS_TO_INCHES = 0.393701
    INCHES_TO_CENTIMETERS = 2.54

    @staticmethod
    def km_to_miles(km):
        if not isinstance(km, (int, float)) or math.isnan(km) or math.isinf(km):
            raise ValueError("Input must be a finite number")
        if km < 0:
            raise ValueError("Distance cannot be negative")
        return km * DistanceConverter.KILOMETERS_TO_MILES

    @staticmethod
    def miles_to_km(miles):
        if not isinstance(miles, (int, float)) or math.isnan(miles) or math.isinf(miles):
            raise ValueError("Input must be a finite number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * DistanceConverter.MILES_TO_KILOMETERS

    @staticmethod
    def m_to_ft(meters):
        if not isinstance(meters, (int, float)) or math.isnan(meters) or math.isinf(meters):
            raise ValueError("Input must be a finite number")
        if meters < 0:
            raise ValueError("Distance cannot be negative")
        return meters * DistanceConverter.METERS_TO_FEET

    @staticmethod
    def ft_to_m(feet):
        if not isinstance(feet, (int, float)) or math.isnan(feet) or math.isinf(feet):
            raise ValueError("Input must be a finite number")
        if feet < 0:
            raise ValueError("Distance cannot be negative")
        return feet * DistanceConverter.FEET_TO_METERS

    @staticmethod
    def cm_to_in(cm):
        if not isinstance(cm, (int, float)) or math.isnan(cm) or math.isinf(cm):
            raise ValueError("Input must be a finite number")
        if cm < 0:
            raise ValueError("Distance cannot be negative")
        return cm * DistanceConverter.CENTIMETERS_TO_INCHES

    @staticmethod
    def in_to_cm(inches):
        if not isinstance(inches, (int, float)) or math.isnan(inches) or math.isinf(inches):
            raise ValueError("Input must be a finite number")
        if inches < 0:
            raise ValueError("Distance cannot be negative")
        return inches * DistanceConverter.INCHES_TO_CENTIMETERS

    @staticmethod
    def convert(value, unit_from, unit_to):
        if unit_from == unit_to:
            return value
        if unit_from == "km" and unit_to == "mi":
            return DistanceConverter.km_to_miles(value)
        if unit_from == "mi" and unit_to == "km":
            return DistanceConverter.miles_to_km(value)
        if unit_from == "m" and unit_to == "ft":
            return DistanceConverter.m_to_ft(value)
        if unit_from == "ft" and unit_to == "m":
            return DistanceConverter.ft_to_m(value)
        if unit_from == "cm" and unit_to == "in":
            return DistanceConverter.cm_to_in(value)
        if unit_from == "in" and unit_to == "cm":
            return DistanceConverter.in_to_cm(value)
        raise ValueError("Unsupported conversion path")

class TestDistanceConverter(unittest.TestCase):
    def test_km_to_miles_positive(self):
        self.assertAlmostEqual(DistanceConverter.km_to_miles(100), 62.1371, places=4)

    def test_km_to_miles_zero(self):
        self.assertEqual(DistanceConverter.km_to_miles(0), 0)

    def test_km_to_miles_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.km_to_miles(-10)

    def test_miles_to_km_positive(self):
        self.assertAlmostEqual(DistanceConverter.miles_to_km(100), 160.934, places=3)

    def test_miles_to_km_zero(self):
        self.assertEqual(DistanceConverter.miles_to_km(0), 0)

    def test_miles_to_km_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.miles_to_km(-5)

    def test_m_to_ft_positive(self):
        self.assertAlmostEqual(DistanceConverter.m_to_ft(100), 328.084, places=3)

    def test_m_to_ft_zero(self):
        self.assertEqual(DistanceConverter.m_to_ft(0), 0)

    def test_m_to_ft_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.m_to_ft(-10)

    def test_ft_to_m_positive(self):
        self.assertAlmostEqual(DistanceConverter.ft_to_m(100), 30.48, places=2)

    def test_ft_to_m_zero(self):
        self.assertEqual(DistanceConverter.ft_to_m(0), 0)

    def test_ft_to_m_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.ft_to_m(-20)

    def test_cm_to_in_positive(self):
        self.assertAlmostEqual(DistanceConverter.cm_to_in(100), 39.3701, places=4)

    def test_cm_to_in_zero(self):
        self.assertEqual(DistanceConverter.cm_to_in(0), 0)

    def test_cm_to_in_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.cm_to_in(-15)

    def test_in_to_cm_positive(self):
        self.assertAlmostEqual(DistanceConverter.in_to_cm(100), 254.0, places=1)

    def test_in_to_cm_zero(self):
        self.assertEqual(DistanceConverter.in_to_cm(0), 0)

    def test_in_to_cm_negative(self):
        with self.assertRaises(ValueError):
            DistanceConverter.in_to_cm(-10)

    def test_convert_same_units(self):
        self.assertEqual(DistanceConverter.convert(50, "km", "km"), 50)

    def test_convert_km_to_mi(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "km", "mi"), 0.621371, places=6)

    def test_convert_mi_to_km(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "mi", "km"), 1.60934, places=5)

    def test_convert_m_to_ft(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "m", "ft"), 3.28084, places=5)

    def test_convert_ft_to_m(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "ft", "m"), 0.3048, places=4)

    def test_convert_cm_to_in(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "cm", "in"), 0.393701, places=6)

    def test_convert_in_to_cm(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, "in", "cm"), 2.54, places=2)

    def test_convert_invalid_path(self):
        with self.assertRaises(ValueError):
            DistanceConverter.convert(10, "km", "ft")

    def test_convert_nan_input(self):
        with self.assertRaises(ValueError):
            DistanceConverter.convert(float('nan'), "km", "mi")

    def test_convert_infinite_input(self):
        with self.assertRaises(ValueError):
            DistanceConverter.convert(float('inf'), "m", "ft")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(100, "km", "mi"))
    print(converter.convert(50, "mi", "km"))
    print(converter.convert(10, "m", "ft"))
    print(converter.convert(100, "ft", "m"))
    print(converter.convert(50, "cm", "in"))
    print(converter.convert(10, "in", "cm"))
    unittest.main()