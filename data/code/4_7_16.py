import unittest

class DistanceConverter:
    """A class to convert distances between kilometers (km) and miles."""
    
    def __init__(self):
        self.kilometers = 0.0
        self.miles = 0.0
    
    def set_kilometers(self, value: float) -> None:
        """Set the distance in kilometers."""
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a number.")
        self.kilometers = abs(value)
    
    def get_miles_from_km(self, km_value: float) -> float:
        """Convert kilometers to miles using the standard conversion factor."""
        if not isinstance(km_value, (int, float)):
            raise TypeError("Input must be a number.")
        return 0.621371 * abs(km_value)
    
    def set_miles(self, value: float) -> None:
        """Set the distance in miles."""
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a number.")
        self.miles = abs(value)
    
    def get_kilometers_from_mi(self, mi_value: float) -> float:
        """Convert miles to kilometers using the standard conversion factor."""
        if not isinstance(mi_value, (int, float)):
            raise TypeError("Input must be a number.")
        return 1.60934 * abs(mi_value)

class TestDistanceConverter(unittest.TestCase):

    def setUp(self) -> None:
        """Initialize the converter for each test method."""
        self.converter = DistanceConverter()
    
    # --- Tests for set_kilometers and get_miles_from_km ---
    def test_set_kilometers_valid_float_positive(self) -> None:
        """Test setting a valid positive float value in kilometers."""
        self.converter.set_kilometers(5.0)
        expected = 3.106855
        result = abs(self.converter.get_miles_from_km(5.0))
        # Allow small floating point discrepancies within tolerance of ~1e-9
        self.assertAlmostEqual(result, expected, delta=1e-7)

    def test_set_kilometers_valid_int_positive(self) -> None:
        """Test setting a valid positive integer value in kilometers."""
        self.converter.set_kilometers(10)
        expected = 6.21371
        result = abs(self.converter.get_miles_from_km(10))
        self.assertAlmostEqual(result, expected, delta=1e-7)

    def test_set_kilometer_zero(self) -> None:
        """Test setting zero kilometers and converting to miles."""
        self.converter.set_kilometers(0.0)
        result = abs(self.converter.get_miles_from_km(0))
        self.assertEqual(result, 0.0)

    def test_set_kilometers_negative_value_handling(self) -> None:
        """Test that negative input is handled by taking absolute value."""
        # The logic uses abs(), so -5 km should behave like 5 km for conversion magnitude
        self.converter.set_kilometers(-10.0)
        expected = 6.21371
        result = abs(self.converter.get_miles_from_km(-10))
        self.assertAlmostEqual(result, expected, delta=1e-7)

    def test_get_miles_invalid_input_type(self) -> None:
        """Test that non-number input raises TypeError."""
        with self.assertRaises(TypeError):
            self.converter.set_kilometers("invalid")
        
    # --- Tests for set_miles and get_kilometers_from_mi ---
    def test_set_miles_valid_float_positive(self) -> None:
        """Test setting a valid positive float value in miles."""
        self.converter.set_miles(10.5)
        expected = 16.9842735
        result = abs(self.converter.get_kilometers_from_mi(10.5))
        self.assertAlmostEqual(result, expected, delta=1e-7)

    def test_set_miles_valid_int_positive(self) -> None:
        """Test setting a valid positive integer value in miles."""
        self.converter.set_miles(20)
        expected = 32.1869455
        result = abs(self.converter.get_kilometers_from_mi(20))
        self.assertAlmostEqual(result, expected, delta=1e-7)

    def test_set_miles_zero(self) -> None:
        """Test setting zero miles and converting to kilometers."""
        self.converter.set_miles(0.0)
        result = abs(self.converter.get_kilometers_from_mi(0))
        self.assertEqual(result, 0.0)

    def test_get_km_invalid_input_type(self) -> None:
        """Test that non-number input raises TypeError."""
        with self.assertRaises(TypeError):
            self.converter.set_miles("bad")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the suite runs without user input, stdin, or files.
    
    def run_sample_checks():
        print("--- Running Sample Verification Checks ---")
        
        converter = DistanceConverter()
        
        # Scenario 1: Convert specific known distance from km to miles
        test_km_value = 50.436726