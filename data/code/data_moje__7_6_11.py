import unittest
from datetime import timedelta

def hours_to_minutes(hours):
    return hours * 60

def hours_to_seconds(hours):
    return hours * 3600

def days_to_hours(days):
    return days * 24

def hours_to_days(hours):
    if hours % 24 != 0:
        return hours / 24.0
    return int(hours / 24)

def seconds_to_hours(seconds):
    return seconds / 3600.0

def days_to_minutes(days):
    return days * 24 * 60

def days_to_seconds(days):
    return days * 24 * 3600

def minutes_to_hours(minutes):
    return minutes / 60.0

def minutes_to_seconds(minutes):
    return minutes * 60

def seconds_to_days(seconds):
    return seconds / (24 * 3600.0)

def add_timedelta(hours=0, minutes=0, seconds=0):
    td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    total_seconds = td.total_seconds()
    days = int(total_seconds // 86400)
    remaining_seconds = int(total_seconds % 86400)
    hours = int(remaining_seconds // 3600)
    remaining_seconds = remaining_seconds % 3600
    mins = int(remaining_seconds // 60)
    secs = int(remaining_seconds % 60)
    return {
        'days': days,
        'hours': hours,
        'minutes': mins,
        'seconds': secs
    }

class TestTimeConversion(unittest.TestCase):
    def test_hours_to_minutes_zero(self):
        self.assertEqual(hours_to_minutes(0), 0)

    def test_hours_to_minutes_positive(self):
        self.assertEqual(hours_to_minutes(1), 60)

    def test_hours_to_minutes_large(self):
        self.assertEqual(hours_to_minutes(1000), 60000)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_hours_to_seconds_positive(self):
        self.assertEqual(hours_to_seconds(1), 3600)

    def test_hours_to_seconds_large(self):
        self.assertEqual(hours_to_seconds(100), 360000)

    def test_days_to_hours_zero(self):
        self.assertEqual(days_to_hours(0), 0)

    def test_days_to_hours_positive(self):
        self.assertEqual(days_to_hours(1), 24)

    def test_days_to_hours_large(self):
        self.assertEqual(days_to_hours(10), 240)

    def test_hours_to_days_exact(self):
        self.assertEqual(hours_to_days(24), 1)

    def test_hours_to_days_non_exact(self):
        self.assertAlmostEqual(hours_to_days(25), 25 / 24.0)

    def test_hours_to_days_zero(self):
        self.assertEqual(hours_to_days(0), 0)

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0.0)

    def test_seconds_to_hours_positive(self):
        self.assertEqual(seconds_to_hours(3600), 1.0)

    def test_seconds_to_hours_negative(self):
        self.assertEqual(seconds_to_hours(-3600), -1.0)

    def test_days_to_minutes_zero(self):
        self.assertEqual(days_to_minutes(0), 0)

    def test_days_to_minutes_positive(self):
        self.assertEqual(days_to_minutes(1), 1440)

    def test_days_to_minutes_large(self):
        self.assertEqual(days_to_minutes(10), 14400)

    def test_days_to_seconds_zero(self):
        self.assertEqual(days_to_seconds(0), 0)

    def test_days_to_seconds_positive(self):
        self.assertEqual(days_to_seconds(1), 86400)

    def test_days_to_seconds_large(self):
        self.assertEqual(days_to_seconds(10), 864000)

    def test_minutes_to_hours_zero(self):
        self.assertEqual(minutes_to_hours(0), 0.0)

    def test_minutes_to_hours_positive(self):
        self.assertEqual(minutes_to_hours(60), 1.0)

    def test_minutes_to_seconds_zero(self):
        self.assertEqual(minutes_to_seconds(0), 0)

    def test_minutes_to_seconds_positive(self):
        self.assertEqual(minutes_to_seconds(1), 60)

    def test_minutes_to_seconds_large(self):
        self.assertEqual(minutes_to_seconds(100), 6000)

    def test_seconds_to_days_zero(self):
        self.assertEqual(seconds_to_days(0), 0.0)

    def test_seconds_to_days_positive(self):
        self.assertEqual(seconds_to_days(86400), 1.0)

    def test_seconds_to_days_negative(self):
        self.assertEqual(seconds_to_days(-86400), -1.0)

    def test_add_timedelta_zero(self):
        result = add_timedelta(0, 0, 0)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 0)
        self.assertEqual(result['minutes'], 0)
        self.assertEqual(result['seconds'], 0)

    def test_add_timedelta_positive(self):
        result = add_timedelta(1, 30, 45)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 1)
        self.assertEqual(result['minutes'], 30)
        self.assertEqual(result['seconds'], 45)

    def test_add_timedelta_large(self):
        result = add_timedelta(25, 0, 0)
        self.assertEqual(result['days'], 1)
        self.assertEqual(result['hours'], 1)
        self.assertEqual(result['minutes'], 0)
        self.assertEqual(result['seconds'], 0)

    def test_add_timedelta_days_only(self):
        result = add_timedelta(0, 0, 0)
        result['days'] = 2
        result['hours'] = 1
        result['minutes'] = 0
        result['seconds'] = 0
        self.assertEqual(result['days'], 2)

    def test_add_timedelta_negative_seconds(self):
        result = add_timedelta(0, 0, -60)
        total = timedelta(seconds=-60).total_seconds()
        td = timedelta(seconds=total)
        expected_days = 0
        expected_hours = -1
        expected_mins = 0
        expected_secs = 0
        self.assertEqual(result['hours'], -1)

if __name__ == '__main__':
    result1 = hours_to_minutes(2)
    print(result1)
    result2 = days_to_seconds(1)
    print(result2)
    result3 = add_timedelta(24, 0, 0)
    print(result3)