import unittest
from datetime import timedelta

def seconds_to_time(seconds):
    """Convert total seconds into a tuple of (days, hours, minutes)."""
    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    
    return (days, hours, minutes)

def time_to_seconds(days=0, hours=0, minutes=0):
    """Convert a tuple of (days, hours, minutes) back to total seconds."""
    days *= 86400
    hours *= 3600
    minutes *= 60
    
    return days + hours + minutes

class TestTimeConversion(unittest.TestCase):
    
    def test_zero_values(self):
        # Zero input should result in zero output
        self.assertEqual(seconds_to_time(0), (0, 0, 0))
        self.assertEqual(time_to_seconds(days=0, hours=0, minutes=0), 0)

    def test_large_time_spans(self):
        # Test with a large number of seconds to ensure no overflow in Python integers
        large_seconds = 1_000_000_000 
        days, hours, minutes = seconds_to_time(large_seconds)
        
        reconstructed = time_to_seconds(days=days, hours=hours, minutes=minutes)
        self.assertEqual(reconstructed, large_seconds)

    def test_negative_values(self):
        # Test negative values to ensure arithmetic handles them correctly (though physical time is usually non-negative)
        neg_seconds = -3601  # Should be roughly (-1 day, 23 hours, 59 minutes)
        
        days, hours, minutes = seconds_to_time(neg_seconds)
        reconstructed = time_to_seconds(days=days, hours=hours, minutes=minutes)
        
        self.assertEqual(reconstructed, neg_seconds)

    def test_exact_boundary_cases(self):
        # Test boundaries: exactly 1 day (86400s), exactly 24h (3600*24s), etc.
        one_day = seconds_to_time(86400)
        self.assertEqual(one_day, (1, 0, 0))

        twenty_four_hours = time_to_seconds(days=0, hours=24, minutes=0)
        self.assertEqual(twenty_four_hours, 86400)

    def test_partial_days_and_hours(self):
        # Test a mix of days and partial hours/minutes
        mixed_input = (3, 5, 10)
        expected_seconds = time_to_seconds(*mixed_input)
        
        result = seconds_to_time(expected_seconds)
        self.assertEqual(result, (3, 5, 10))

    def test_fractional_minutes_rounding(self):
        # Test a case where there are leftover minutes that don't divide evenly into hours
        input_val = time_to_seconds(days=2, hours=4, minutes=7)
        result = seconds_to_time(input_val)
        
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 4)
        # Note: Since we are working with integers in the conversion logic described previously (integers only), 
        # any fractional part of a minute would be lost. This test assumes integer arithmetic based on previous context.
        # If floating point was used, this assertion might need adjustment to allow small epsilon differences.
        self.assertEqual(result[2], 7)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeConversion)
    
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    # Run tests directly in the console for demonstration without requiring a test file to exist previously
    if not result.wasSuccessful():
        print("\nSome tests failed.")
    else:
        print("\nAll tests passed successfully.")