import unittest

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

class TimeConverter:
    def __init__(self):
        self._seconds_per_hour = SECONDS_PER_HOUR
        self._seconds_per_minute = SECONDS_PER_MINUTE

    def to_hms(self, total_seconds):
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be a number")
        if total_seconds < 0:
            raise ValueError("Input cannot be negative")
        
        total_seconds = int(total_seconds)
        hours = total_seconds // self._seconds_per_hour
        remaining = total_seconds % self._seconds_per_hour
        minutes = remaining // self._seconds_per_minute
        seconds = remaining % self._seconds_per_minute
        return hours, minutes, seconds

    def from_hms(self, hours, minutes, seconds):
        if not all(isinstance(x, (int, float)) for x in [hours, minutes, seconds]):
            raise TypeError("All inputs must be numbers")
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components cannot be negative")
        return hours * self._seconds_per_hour + minutes * self._seconds_per_minute + int(seconds)

class TestTimeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TimeConverter()

    def test_zero_input(self):
        self.assertEqual(self.converter.to_hms(0), (0, 0, 0))
        self.assertEqual(self.converter.from_hms(0, 0, 0), 0)

    def test_exact_hour(self):
        self.assertEqual(self.converter.to_hms(3600), (1, 0, 0))
        self.assertEqual(self.converter.from_hms(1, 0, 0), 3600)

    def test_exact_minute(self):
        self.assertEqual(self.converter.to_hms(60), (0, 1, 0))
        self.assertEqual(self.converter.from_hms(0, 1, 0), 60)

    def test_largest_span(self):
        large_seconds = 86400 * 365 + 12345
        result = self.converter.to_hms(large_seconds)
        expected_hours = 8760 + 3
        self.assertEqual(result, (expected_hours, 20, 45))
        self.assertEqual(self.converter.from_hms(*result), large_seconds)

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.converter.to_hms(-10)
        with self.assertRaises(ValueError):
            self.converter.from_hms(1, -1, 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            self.converter.to_hms("100")
        with self.assertRaises(TypeError):
            self.converter.from_hms(1, "2", 3)

    def test_float_handling(self):
        self.assertEqual(self.converter.to_hms(3661.9), (1, 1, 1))
        self.assertEqual(self.converter.from_hms(0, 0, 1.9), 1)

if __name__ == '__main__':
    print("Running Unit Tests...")
    unittest.main(exit=False, verbosity=2)
    converter = TimeConverter()
    sample_seconds = 3725
    hms_result = converter.to_hms(sample_seconds)
    print(f"Converted {sample_seconds} seconds to {hms_result}")
    h, m, s = hms_result
    back_to_seconds = converter.from_hms(h, m, s)
    print(f"Converted back to {back_to_seconds} seconds")
    edge_case = 0
    zero_result = converter.to_hms(edge_case)
    print(f"Edge case (0) result: {zero_result}")
    large_span = 90061
    large_result = converter.to_hms(large_span)
    print(f"Large span ({large_span}) result: {large_result}")