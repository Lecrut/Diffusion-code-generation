import unittest
def time_to_minutes(time_value):
    return time_value * 60
class TestTimeToMinutes(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(time_to_minutes(0), 0)
    def test_positive_integer_time(self):
        self.assertEqual(time_to_minutes(5), 300)
        self.assertEqual(time_to_minutes(1), 60)
    def test_large_time(self):
        self.assertEqual(time_to_minutes(1000), 60000)
    def test_maximum_value_example(self):
        self.assertEqual(time_to_minutes(24), 1440)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)