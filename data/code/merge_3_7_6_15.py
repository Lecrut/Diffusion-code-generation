import unittest
from datetime import timedelta

def seconds_to_time(seconds):
    """Convert total seconds into a time object (days, hours, minutes)."""
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or float representing seconds.")
    
    days = int(seconds // 86400)
    remaining_seconds = seconds % 86400
    
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    
    minutes = int(remaining_seconds // 60)
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes
    }

def time_to_seconds(time_dict):
    """Convert a dictionary of days, hours, and minutes back to total seconds."""
    if not isinstance(time_dict, dict):
        raise TypeError("Input must be a dictionary with keys: 'days', 'hours', 'minutes'.")
    
    required_keys = {'days', 'hours', 'minutes'}
    if not all(key in time_dict for key in required_keys):
        raise ValueError(f"Missing required keys. Expected {required_keys}, got {set(time_dict.keys())}")

    days, hours, minutes = int(time_dict['days']), int(time_dict['hours']), int(time_dict['minutes'])
    
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60)
    return float(total_seconds)

class TestTimeConversion(unittest.TestCase):

    def test_zero_values(self):
        """Test handling of zero input."""
        result = seconds_to_time(0.0)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 0)
        self.assertEqual(result['minutes'], 0)
        
        back_to_seconds = time_to_seconds({'days': 0, 'hours': 0, 'minutes': 0})
        self.assertAlmostEqual(back_to_seconds, 0.0)

    def test_large_time_spans(self):
        """Test handling of large time spans."""
        # A span representing roughly the age of the universe in seconds (approximated for testing)
        huge_seconds = float('inf') if hasattr(float, 'inf') else None
        
        # Use a very large finite number instead to avoid infinity issues in basic arithmetic tests unless specifically needed.
        # Let's use 10^9 seconds (about 31 years).
        test_large_input = 10**9 
        result = seconds_to_time(test_large_input)
        
        expected_days = int(10**9 // 86400)
        remaining_after_days = float(10**9 % 86400)
        expected_hours = int(remaining_after_days // 3600)
        remaining_after_hours = float(remaining_after_days % 3600)
        expected_minutes = int(remaining_after_hours // 60)

        self.assertEqual(result['days'], expected_days)
        self.assertEqual(result['hours'], expected_hours)
        self.assertEqual(result['minutes'], expected_minutes)
        
        # Verify round trip for large numbers with floating point precision check where applicable, 
        # though integers should be exact. Since input was float in test_large_input but int logic applies:
        back_to_seconds = time_to_seconds({
            'days': result['days'],
            'hours': result['hours'],
            'minutes': result['minutes']
        })
        
        self.assertEqual(back_to_seconds, 10**9)

    def test_negative_values(self):
        """Test handling of negative values."""
        # Negative seconds should be handled logically (though physically time doesn't go back this way in simple math).
        neg_input = -3665.5
        
        result = seconds_to_time(neg_input)
        
        expected_days = int(-1 // 86400) if isinstance(int, type(lambda: None)) else int(neg_input // 86400) 
        # Python's integer division rounds towards negative infinity for negatives.
        # -3665 / 86400 is approx -0.042 -> floor is -1? No wait.
        # Let's re-evaluate logic: int(-0.042) in Python is 0 because it truncates towards zero if cast directly, 
        # but // operator floors. The function uses //.
        
        days = neg_input // 86400
        remaining_seconds = neg_input % 86400
        
        hours = int(remaining_seconds / 3600)
        minutes = int((remaining_seconds - (hours * 3600)) / 60)

        # Re-calculate expected manually to ensure test correctness against function logic
        days_val = neg_input // 86400
        rem_after_days = neg_input % 86400
        
        hours_val = int(rem_after_days / 3600)
        rem_after_hours = rem_after_days - (hours_val * 3600)
        
        minutes_val = int(rem_after_hours / 60)

        self.assertEqual(result['days'], days_val)
        # Note: Behavior of % with negative numbers in Python keeps sign same as divisor? 
        # No, remainder has same sign as divisor (positive). So -3665.5 % 86400 is positive small number.
        
    def test_type_errors(self):
        """Test handling of invalid input types."""
        with self.assertRaises(TypeError):
            seconds_to_time("invalid string")
            
        with self.assertRaises(ValueError):
            time_to_seconds({"days": 1, "hours": 2}) # Missing 'minutes'

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeConversion)
    
    # Run the tests directly to ensure they execute without command line args or input prompts.
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    if __name__ == '__main__':
        print("Running sample test suite...")
        
        # Hard-coded manual checks for demonstration within the block logic before running full suite
        # This ensures no external dependencies or inputs are needed.
        
        try:
            r1 = seconds_to_time(0)
            assert r1 == {'days': 0, 'hours': 0, 'minutes': 0}, "Zero test failed"
            
            r2 = time_to_seconds({'days': 5, 'hours': 30, 'minutes': 45})
            expected_r2 = (5 * 86400) + (30 * 3600) + (45 * 60)
            assert r2 == expected_r2, f"Round trip test failed: {r2} != {expected_r2}"
            
            print("Sample manual checks passed.")
        except Exception as e:
            print(f"Manual check error: {e}")

    # The actual unit testing framework execution happens here via the suite runner above.