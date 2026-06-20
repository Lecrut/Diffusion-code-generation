import unittest

def hours_to_seconds(hours):
    return hours * 3600

def days_to_seconds(days):
    return days * 86400

def seconds_to_hours(seconds):
    return seconds / 3600

class TestTimeConversions(unittest.TestCase):
    def test_hours_to_seconds_zero(self):
        result = hours_to_seconds(0)
        self.assertEqual(result, 0)

    def test_hours_to_seconds_small_value(self):
        result = hours_to_seconds(1)
        self.assertEqual(result, 3600)

    def test_hours_to_seconds_large_value(self):
        result = hours_to_seconds(1000000)
        self.assertEqual(result, 3600000000)

    def test_days_to_seconds_zero(self):
        result = days_to_seconds(0)
        self.assertEqual(result, 0)

    def test_days_to_seconds_small_value(self):
        result = days_to_seconds(1)
        self.assertEqual(result, 86400)

    def test_days_to_seconds_large_value(self):
        result = days_to_seconds(500000)
        self.assertEqual(result, 43200000000)

    def test_seconds_to_hours_zero(self):
        result = seconds_to_hours(0)
        self.assertEqual(result, 0.0)

    def test_seconds_to_hours_small_value(self):
        result = seconds_to_hours(3600)
        self.assertEqual(result, 1.0)

    def test_seconds_to_hours_large_value(self):
        result = seconds_to_hours(864000000)
        self.assertEqual(result, 240000.0)

if __name__ == '__main__':
    unittest.main()