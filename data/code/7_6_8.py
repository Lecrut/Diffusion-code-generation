import unittest
class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(self.convert_seconds_to_minutes(0), 0.0)
        self.assertEqual(self.convert_seconds_to_minutes(60), 1.0)
        self.assertEqual(self.convert_seconds_to_minutes(3599), 59.98333333333333)
        self.assertEqual(self.convert_seconds_to_minutes(3600), 60.0)
    def test_minutes_to_seconds(self):
        self.assertEqual(self.convert_minutes_to_seconds(0), 0.0)
        self.assertEqual(self.convert_minutes_to_seconds(60), 60.0)
        self.assertEqual(self.convert_minutes_to_seconds(120), 120.0)
        self.assertEqual(self.convert_minutes_to_seconds(1.5), 90.0)
    def test_hours_to_minutes(self):
        self.assertEqual(self.convert_hours_to_minutes(0), 0.0)
        self.assertEqual(self.convert_hours_to_minutes(1), 60.0)
        self.assertEqual(self.convert_hours_to_minutes(2), 120.0)
        self.assertEqual(self.convert_hours_to_minutes(24), 1440.0)
        self.assertEqual(self.convert_hours_to_minutes(12.5), 750.0)
    def test_minutes_to_hours(self):
        self.assertEqual(self.convert_minutes_to_hours(0), 0.0)
        self.assertEqual(self.convert_minutes_to_hours(60), 1.0)
        self.assertEqual(self.convert_minutes_to_hours(120), 2.0)
        self.assertEqual(self.convert_minutes_to_hours(1440), 24.0)
        self.assertEqual(self.convert_minutes_to_hours(1.5), 0.25)
    def test_large_time_spans(self):
        self.assertEqual(self.convert_seconds_to_minutes(86400), 1440.0)
        self.assertEqual(self.convert_minutes_to_hours(100800), 1680.0)
        self.assertEqual(self.convert_hours_to_minutes(480), 28800.0)
if __name__ == '__main__':
    def convert_seconds_to_minutes(seconds):
        return seconds / 60.0
    def convert_minutes_to_seconds(minutes):
        return minutes * 60.0
    def convert_hours_to_minutes(hours):
        return hours * 60.0
    unittest.main(argv=['first-arg-action', 'excite'], exit=False)