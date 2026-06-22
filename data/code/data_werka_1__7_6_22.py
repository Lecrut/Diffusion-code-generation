import unittest

def seconds_to_minutes(seconds):
    return seconds // 60

def minutes_to_hours(minutes):
    return minutes // 60

def hours_to_days(hours):
    return hours // 24

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_minutes(self):
        self.assertEqual(seconds_to_minutes(0), 0)
        self.assertEqual(seconds_to_minutes(59), 0)
        self.assertEqual(seconds_to_minutes(60), 1)
        self.assertEqual(seconds_to_minutes(3600), 60)

    def test_minutes_to_hours(self):
        self.assertEqual(minutes_to_hours(0), 0)
        self.assertEqual(minutes_to_hours(59), 0)
        self.assertEqual(minutes_to_hours(60), 1)
        self.assertEqual(minutes_to_hours(1440), 24)

    def test_hours_to_days(self):
        self.assertEqual(hours_to_days(0), 0)
        self.assertEqual(hours_to_days(23), 0)
        self.assertEqual(hours_to_days(24), 1)
        self.assertEqual(hours_to_days(8760), 365)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(seconds_to_minutes(3660))
    print(minutes_to_hours(1441))
    print(hours_to_days(8761))