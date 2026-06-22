import unittest
from datetime import timedelta

def hours_to_minutes(hours: float) -> float:
    return hours * 60

def hours_to_seconds(hours: float) -> float:
    return hours * 3600

def minutes_to_hours(minutes: float) -> float:
    return minutes / 60

def minutes_to_seconds(minutes: float) -> float:
    return minutes * 60

def seconds_to_hours(seconds: float) -> float:
    return seconds / 3600

def seconds_to_minutes(seconds: float) -> float:
    return seconds / 60

def days_to_hours(days: int) -> int:
    return days * 24

def days_to_seconds(days: int) -> int:
    return days * 86400

def hours_to_days(hours: float) -> float:
    return hours / 24

class TestTimeConversion(unittest.TestCase):
    def test_hours_to_minutes_basic(self):
        self.assertEqual(hours_to_minutes(1), 60)

    def test_hours_to_minutes_zero(self):
        self.assertEqual(hours_to_minutes(0), 0)

    def test_hours_to_minutes_large(self):
        self.assertEqual(hours_to_minutes(1000), 60000)

    def test_hours_to_seconds_basic(self):
        self.assertEqual(hours_to_seconds(1), 3600)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_hours_to_seconds_large(self):
        self.assertEqual(hours_to_seconds(100), 360000)

    def test_minutes_to_hours_basic(self):
        self.assertEqual(minutes_to_hours(60), 1.0)

    def test_minutes_to_hours_zero(self):
        self.assertEqual(minutes_to_hours(0), 0.0)

    def test_minutes_to_hours_large(self):
        self.assertAlmostEqual(minutes_to_hours(3600), 60.0)

    def test_minutes_to_seconds_basic(self):
        self.assertEqual(minutes_to_seconds(1), 60)

    def test_minutes_to_seconds_zero(self):
        self.assertEqual(minutes_to_seconds(0), 0)

    def test_minutes_to_seconds_large(self):
        self.assertEqual(minutes_to_seconds(100), 6000)

    def test_seconds_to_hours_basic(self):
        self.assertEqual(seconds_to_hours(3600), 1.0)

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0.0)

    def test_seconds_to_hours_large(self):
        self.assertAlmostEqual(seconds_to_hours(7200), 2.0)

    def test_seconds_to_minutes_basic(self):
        self.assertEqual(seconds_to_minutes(60), 1.0)

    def test_seconds_to_minutes_zero(self):
        self.assertEqual(seconds_to_minutes(0), 0.0)

    def test_seconds_to_minutes_large(self):
        self.assertAlmostEqual(seconds_to_minutes(120), 2.0)

    def test_days_to_hours_basic(self):
        self.assertEqual(days_to_hours(1), 24)

    def test_days_to_hours_zero(self):
        self.assertEqual(days_to_hours(0), 0)

    def test_days_to_hours_large(self):
        self.assertEqual(days_to_hours(10), 240)

    def test_days_to_seconds_basic(self):
        self.assertEqual(days_to_seconds(1), 86400)

    def test_days_to_seconds_zero(self):
        self.assertEqual(days_to_seconds(0), 0)

    def test_days_to_seconds_large(self):
        self.assertEqual(days_to_seconds(2), 172800)

    def test_hours_to_days_basic(self):
        self.assertEqual(hours_to_days(24), 1.0)

    def test_hours_to_days_zero(self):
        self.assertEqual(hours_to_days(0), 0.0)

    def test_hours_to_days_large(self):
        self.assertAlmostEqual(hours_to_days(48), 2.0)

    def test_complex_conversion_chain(self):
        self.assertAlmostEqual(hours_to_minutes(1.5), 90)
        self.assertAlmostEqual(minutes_to_seconds(90), 5400)
        self.assertAlmostEqual(seconds_to_hours(5400), 1.5)
        self.assertAlmostEqual(hours_to_days(1.5), 0.0625)
        self.assertAlmostEqual(days_to_hours(1), 24)

if __name__ == '__main__':
    result1 = hours_to_minutes(2)
    result2 = minutes_to_seconds(30)
    result3 = seconds_to_hours(7200)
    result4 = days_to_seconds(3)
    result5 = hours_to_days(72)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)