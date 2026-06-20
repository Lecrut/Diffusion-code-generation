import unittest

def seconds_to_days_hours_minutes(seconds):
    if seconds < 0:
        raise ValueError("Negative seconds not allowed")
    days = seconds // 86400
    remaining = seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    return days, hours, minutes

def days_hours_minutes_to_seconds(days, hours, minutes):
    if days < 0 or hours < 0 or minutes < 0:
        raise ValueError("Negative values not allowed")
    if hours >= 24 or minutes >= 60:
        raise ValueError("Hours must be < 24 and minutes < 60")
    total = (days * 86400) + (hours * 3600) + (minutes * 60)
    return total

class TestTimeConversion(unittest.TestCase):
    def test_zero_seconds(self):
        self.assertEqual(seconds_to_days_hours_minutes(0), (0, 0, 0))
    
    def test_small_value(self):
        self.assertEqual(seconds_to_days_hours_minutes(3665), (0, 1, 1))
    
    def test_exact_hour(self):
        self.assertEqual(seconds_to_days_hours_minutes(3600), (0, 1, 0))
    
    def test_exact_day(self):
        self.assertEqual(seconds_to_days_hours_minutes(86400), (1, 0, 0))
    
    def test_large_value(self):
        self.assertEqual(seconds_to_days_hours_minutes(172800), (2, 0, 0))
    
    def test_mixed_large_value(self):
        self.assertEqual(seconds_to_days_hours_minutes(90061), (1, 1, 0))
    
    def test_negative_seconds(self):
        with self.assertRaises(ValueError):
            seconds_to_days_hours_minutes(-1)
    
    def test_reverse_conversion_zero(self):
        self.assertEqual(days_hours_minutes_to_seconds(0, 0, 0), 0)
    
    def test_reverse_conversion_small(self):
        self.assertEqual(days_hours_minutes_to_seconds(0, 1, 1), 3660)
    
    def test_reverse_conversion_large(self):
        self.assertEqual(days_hours_minutes_to_seconds(100, 23, 59), 8639940)
    
    def test_invalid_hours(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_to_seconds(0, 24, 0)
    
    def test_invalid_minutes(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_to_seconds(0, 0, 60)
    
    def test_negative_days(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_to_seconds(-1, 0, 0)

if __name__ == '__main__':
    result = seconds_to_days_hours_minutes(90061)
    print(result)
    total_seconds = days_hours_minutes_to_seconds(1, 1, 0)
    print(total_seconds)
    unittest.main()