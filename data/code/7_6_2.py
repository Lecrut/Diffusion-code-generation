import unittest
class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(self.convert_seconds_to_minutes(0), 0.0)
        self.assertEqual(self.convert_seconds_to_minutes(60), 1.0)
        self.assertEqual(self.convert_seconds_to_minutes(3600), 60.0)
        self.assertEqual(self.convert_seconds_to_minutes(3661), 61.01666666666666)
    def test_minutes_to_seconds(self):
        self.assertEqual(self.convert_minutes_to_seconds(0), 0.0)
        self.assertEqual(self.convert_minutes_to_seconds(60), 60.0)
        self.assertEqual(self.convert_minutes_to_seconds(120), 120.0)
        self.assertEqual(self.convert_minutes_to_seconds(1.5), 90.0)
    def test_large_time_spans(self):
        self.assertEqual(self.convert_seconds_to_minutes(86400), 1440.0)
        self.assertEqual(self.convert_seconds_to_minutes(3600 * 24 * 30), 259200.0)
        self.assertEqual(self.convert_seconds_to_minutes(86400 * 1000), 1440000.0)
    def test_mixed_conversion(self):
        self.assertEqual(self.convert_seconds_to_minutes(125), 2.0833333333333335)
        self.assertEqual(self.convert_minutes_to_seconds(1.5), 90.0)
if __name__ == '__main__':
    def convert_seconds_to_minutes(seconds):
        return seconds / 60.0
    def convert_minutes_to_seconds(minutes):
        return minutes * 60.0
    unittest.main(argv=['first-arg-is-ignored'], exit=False)