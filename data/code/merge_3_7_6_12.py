import unittest
from datetime import timedelta

class TimeConversion:
    """Utility class to handle time conversion between seconds, minutes, hours."""

    @staticmethod
    def convert_seconds_to_hours(seconds: float) -> dict:
        """Convert total seconds into a dictionary containing hours, remaining minutes, and remaining seconds.

        Args:
            seconds (float): Total number of seconds as an integer or positive float.

        Returns:
            dict: Keys 'hours', 'minutes', and 'seconds' representing the converted time components.
        """
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")

        total_seconds = int(round(seconds))
        hours = total_seconds // 3600
        remaining_after_hours = total_seconds % 3600
        minutes = remaining_after_hours // 60
        final_remaining_seconds = remaining_after_hours % 60

        return {
            "hours": hours,
            "minutes": minutes,
            "seconds": float(final_remaining_seconds)
        }

class TestTimeConversion(unittest.TestCase):
    """Test suite for TimeConversion functions."""

    def test_zero_input(self):
        """Ensure zero input returns all zeros correctly."""
        result = TimeConversion.convert_seconds_to_hours(0)
        self.assertEqual(result["hours"], 0)
        self.assertEqual(result["minutes"], 0)
        self.assertAlmostEqual(result["seconds"], 0.0, places=1)

    def test_large_time_span(self):
        """Ensure large time spans are handled without overflow or precision loss."""
        # A span of roughly 2 years in seconds (approximate for testing purposes: ~63 million seconds)
        large_seconds = 63_072_000.5

        result = TimeConversion.convert_seconds_to_hours(large_seconds)
        
        expected_total_seconds = int(round(result["hours"] * 3600 + result["minutes"] * 60)) + round(result["seconds"])
        self.assertEqual(expected_total_seconds, large_seconds)

    def test_integer_input(self):
        """Ensure integer inputs are handled correctly."""
        input_val = 7265.9
        expected_hours = 1
        expected_minutes = 43
        # The fractional part .9 seconds should be preserved as float in output but truncated for exact int check if needed, 
        # however the spec says return seconds as float usually or precise remainder. Let's assume standard behavior:
        result = TimeConversion.convert_seconds_to_hours(input_val)
        
        self.assertEqual(result["hours"], expected_hours)
        self.assertEqual(result["minutes"], expected_minutes)
        # Check that fractional seconds are preserved correctly based on input precision logic (rounded to 1 decimal in class for simplicity or exact)
        self.assertAlmostEqual(abs(result["seconds"] - 0.9), 0, places=2)

    def test_negative_input_handling(self):
        """Ensure negative inputs raise a ValueError."""
        with self.assertRaises(ValueError):
            TimeConversion.convert_seconds_to_hours(-10)

if __name__ == '__main__':
    # Run the tests directly without command-line arguments or user input
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failIfNoSuccesses())