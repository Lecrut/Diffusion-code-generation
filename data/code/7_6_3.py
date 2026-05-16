import unittest
class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(60, 1)
        self.assertEqual(120, 2)
        self.assertEqual(0, 0)
        self.assertEqual(3600, 60)
    def test_minutes_to_seconds(self):
        self.assertEqual(60, 60)
        self.assertEqual(120, 120)
        self.assertEqual(0, 0)
        self.assertEqual(3600, 3600)
    def test_hours_to_minutes(self):
        self.assertEqual(60, 60)
        self.assertEqual(120, 120)
        self.assertEqual(0, 0)
        self.assertEqual(3600, 60)
    def test_seconds_to_hours(self):
        self.assertEqual(3600, 1)
        self.assertEqual(7200, 2)
        self.assertEqual(0, 0)
        self.assertEqual(86400, 24)
    def test_large_time_span(self):
        self.assertEqual(86400 * 10, 10)
        self.assertEqual(86400 * 24, 24)
        self.assertEqual(86400 * 365, 365)
    def test_zero_values(self):
        self.assertEqual(0, 0)
        self.assertEqual(0, 0)
        self.assertEqual(0, 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)