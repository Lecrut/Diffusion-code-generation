import unittest
def convert_time(time_value, unit):
    if unit == 'seconds':
        return time_value
    elif unit == 'minutes':
        return time_value / 60
    elif unit == 'hours':
        return time_value / 3600
    else:
        raise ValueError("Invalid unit")
class TestTimeConversion(unittest.TestCase):
    def test_seconds(self):
        self.assertEqual(convert_time(10, 'seconds'), 10)
        self.assertEqual(convert_time(0, 'seconds'), 0)
        self.assertEqual(convert_time(-5, 'seconds'), -5)
    def test_minutes(self):
        self.assertEqual(convert_time(60, 'minutes'), 1.0)
        self.assertEqual(convert_time(120, 'minutes'), 2.0)
        self.assertEqual(convert_time(0, 'minutes'), 0.0)
        self.assertEqual(convert_time(90, 'minutes'), 1.5)
    def test_hours(self):
        self.assertEqual(convert_time(3600, 'hours'), 1.0)
        self.assertEqual(convert_time(7200, 'hours'), 2.0)
        self.assertEqual(convert_time(0, 'hours'), 0.0)
        self.assertEqual(convert_time(10800, 'hours'), 3.0)
    def test_large_values(self):
        large_seconds = 86400 * 24 * 365                        
        self.assertAlmostEqual(convert_time(large_seconds, 'minutes'), 175333280.0)
        self.assertAlmostEqual(convert_time(large_seconds, 'hours'), 175333280.0)
    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            convert_time(10, 'days')
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)