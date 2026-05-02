import unittest
class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(self.convert_seconds_to_minutes(0), 0.0)
        self.assertEqual(self.convert_seconds_to_minutes(60), 1.0)
        self.assertEqual(self.convert_seconds_to_minutes(3600), 60.0)
        self.assertEqual(self.convert_seconds_to_minutes(3661), 61.01833333333333)
    def test_minutes_to_seconds(self):
        self.assertEqual(self.convert_minutes_to_seconds(0), 0.0)
        self.assertEqual(self.convert_minutes_to_seconds(60), 60.0)
        self.assertEqual(self.convert_minutes_to_seconds(120), 120.0)
        self.assertEqual(self.convert_minutes_to_seconds(90.5), 5450.0)
    def test_large_time_spans(self):
        self.assertEqual(self.convert_seconds_to_minutes(86400), 1440.0)
        self.assertEqual(self.convert_seconds_to_minutes(86400 * 24), 43200.0)
        self.assertEqual(self.convert_seconds_to_minutes(3600 * 24 * 365), 31536000.0)
    def test_zero_values(self):
        self.assertEqual(self.convert_seconds_to_minutes(0), 0.0)
        self.assertEqual(self.convert_minutes_to_seconds(0), 0.0)
    def test_floating_point_precision(self):
        self.assertAlmostEqual(self.convert_seconds_to_minutes(123.45), 2.0575)
        self.assertAlmostEqual(self.convert_minutes_to_seconds(1.5), 90.0)
if __name__ == '__main__':
    def convert_seconds_to_minutes(seconds):
        return seconds / 60.0
    def convert_minutes_to_seconds(minutes):
        return minutes * 60.0
    unittest.main(argv=['first-arg-action', 'excite'], exit=False)