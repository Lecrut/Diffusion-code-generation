import unittest

def seconds_to_days(hours):
    return hours * 3600

def days_to_seconds(days):
    return days * 86400

def total_seconds_to_days(total_seconds):
    return total_seconds / 86400

def total_days_to_seconds(total_days):
    return total_days * 86400

def days_to_hours(days):
    return days * 24

def hours_to_days(hours):
    return hours / 24

def hours_to_seconds(hours):
    return hours * 3600

def seconds_to_hours(seconds):
    return seconds / 3600

class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_days_zero(self):
        self.assertEqual(seconds_to_days(0), 0)

    def test_days_to_seconds_zero(self):
        self.assertEqual(days_to_seconds(0), 0)

    def test_total_seconds_to_days_zero(self):
        self.assertEqual(total_seconds_to_days(0), 0.0)

    def test_total_days_to_seconds_zero(self):
        self.assertEqual(total_days_to_seconds(0), 0)

    def test_days_to_hours_zero(self):
        self.assertEqual(days_to_hours(0), 0)

    def test_hours_to_days_zero(self):
        self.assertEqual(hours_to_days(0), 0.0)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0.0)

    def test_large_seconds_to_days(self):
        self.assertEqual(seconds_to_days(1000000), 3600000000)

    def test_large_days_to_seconds(self):
        self.assertEqual(days_to_seconds(1000000), 86400000000)

    def test_large_total_seconds_to_days(self):
        self.assertEqual(total_seconds_to_days(86400000000), 1000000.0)

    def test_large_total_days_to_seconds(self):
        self.assertEqual(total_days_to_seconds(1000000), 86400000000)

    def test_large_days_to_hours(self):
        self.assertEqual(days_to_hours(1000000), 24000000)

    def test_large_hours_to_days(self):
        self.assertEqual(hours_to_days(24000000), 1000000.0)

    def test_large_hours_to_seconds(self):
        self.assertEqual(hours_to_seconds(1000000), 3600000000)

    def test_large_seconds_to_hours(self):
        self.assertEqual(seconds_to_hours(3600000000), 1000000.0)

    def test_fractional_hours_to_days(self):
        self.assertEqual(hours_to_days(12), 0.5)

    def test_fractional_seconds_to_hours(self):
        self.assertEqual(seconds_to_hours(1800), 0.5)

    def test_fractional_days_to_hours(self):
        self.assertEqual(days_to_hours(0.5), 12.0)

    def test_fractional_total_seconds_to_days(self):
        self.assertEqual(total_seconds_to_days(43200), 0.5)

    def test_fractional_total_days_to_seconds(self):
        self.assertEqual(total_days_to_seconds(0.5), 43200.0)

if __name__ == '__main__':
    unittest.main()
    print(days_to_seconds(30))
    print(seconds_to_days(1000000000))
    print(total_seconds_to_days(864000000))
    print(total_days_to_seconds(10000))
    print(days_to_hours(25))
    print(hours_to_days(48))
    print(hours_to_seconds(10000))
    print(seconds_to_hours(72000))