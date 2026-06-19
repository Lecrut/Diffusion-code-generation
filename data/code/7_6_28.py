import unittest

def seconds_to_hours(seconds):
    return seconds / 3600

def hours_to_seconds(hours):
    return hours * 3600

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0)

    def test_seconds_to_hours_large_value(self):
        self.assertEqual(seconds_to_hours(86400), 24)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_hours_to_seconds_large_value(self):
        self.assertEqual(hours_to_seconds(24), 86400)
if __name__ == '__main__':
    print(seconds_to_hours(3600))
    print(hours_to_seconds(1))
    unittest.main(argv=[''], exit=False)