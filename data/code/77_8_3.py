import unittest
def time_to_minutes(time_value):
    return time_value * 60
class TestTimeToMinutes(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(time_to_minutes(0), 0)
    def test_positive_integer(self):
        self.assertEqual(time_to_minutes(5), 300)
    def test_positive_float(self):
        self.assertAlmostEqual(time_to_minutes(1.5), 90.0)
    def test_maximum_value(self):
        large_time = 1000000
        expected_minutes = 60000000
        self.assertEqual(time_to_minutes(large_time), expected_minutes)
    def test_negative_time(self):
        self.assertEqual(time_to_minutes(-10), -600)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)