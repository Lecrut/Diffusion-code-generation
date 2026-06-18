import unittest
from datetime import timedelta

def seconds_to_time(seconds):
    """Convert total seconds into a time object (days, hours, minutes)."""
    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds % 60
    }

def time_to_seconds(time_dict):
    """Convert a dictionary of time components back to total seconds."""
    d = time_dict.get('days', 0)
    h = time_dict.get('hours', 0)
    m = time_dict.get('minutes', 0)
    s = time_dict.get('seconds', 0)
    
    return (d * 86400) + (h * 3600) + (m * 60) + s

class TestTimeConversion(unittest.TestCase):

    def test_zero_values(self):
        """Test conversion with zero input."""
        self.assertEqual(seconds_to_time(0), {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0})
        result = time_to_seconds({'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0})
        self.assertEqual(result, 0)

    def test_large_time_spans(self):
        """Test conversion with large values."""
        # One year approx (365 days * 86400 seconds = 31,536,000) plus extra hours/minutes
        total_seconds = 31536000 + 23*3600 + 59*60 + 59
        
        result_dict = seconds_to_time(total_seconds)
        
        self.assertEqual(result_dict['days'], 365)
        self.assertEqual(result_dict['hours'], 23)
        self.assertEqual(result_dict['minutes'], 59)
        self.assertEqual(result_dict['seconds'], 59)

    def test_round_trip_conversion(self):
        """Ensure seconds_to_time and time_to_seconds are inverses."""
        original_seconds = 100000
        
        converted_back = time_to_seconds(seconds_to_time(original_seconds))
        
        self.assertEqual(converted_back, original_seconds)

    def test_negative_values_handling(self):
        """Test that negative values do not crash and return expected math results (though logically invalid for physical time)."""
        # While physically impossible, the function should handle it without crashing.
        result = seconds_to_time(-100)
        
        self.assertEqual(result['days'], -1)  # -1 day is roughly correct magnitude-wise in this simple implementation
        
    def test_boundary_conditions(self):
        """Test boundaries like exactly one hour or minute."""
        # Exactly one hour (3600 seconds)
        result = seconds_to_time(3600)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 1)
        self.assertEqual(result['minutes'], 0)
        
        # Exactly one minute (60 seconds)
        result = seconds_to_time(60)
        self.assertEqual(result['seconds'], 0)
        self.assertEqual(result['minutes'], 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeConversion)
    
    # Run the tests directly to ensure they execute without external dependencies or input prompts.
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else result.errors[0][1])