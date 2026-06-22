import unittest

def seconds_to_hours(seconds):
    return seconds / 3600

def hours_to_seconds(hours):
    return hours * 3600

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0)

    def test_seconds_to_hours_positive(self):
        self.assertEqual(seconds_to_hours(3600), 1)
        self.assertEqual(seconds_to_hours(7200), 2)

    def test_seconds_to_hours_large_value(self):
        self.assertEqual(seconds_to_hours(86400), 24)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_hours_to_seconds_positive(self):
        self.assertEqual(hours_to_seconds(1), 3600)
        self.assertEqual(hours_to_seconds(2), 7200)

    def test_hours_to_seconds_large_value(self):
        self.assertEqual(hours_to_seconds(24), 86400)
if __name__ == '__main__':
    print('Seconds to hours (3600):', seconds_to_hours(3600))
    print('Hours to seconds (1):', hours_to_seconds(1))
    unittest.main(argv=[''], exit=False)