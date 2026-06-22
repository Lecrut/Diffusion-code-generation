import unittest
from datetime import timedelta

def seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    hours, remainder = divmod(int(total_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

def hms_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    return hours * 3600 + minutes * 60 + seconds

class TestTimeConversion(unittest.TestCase):
    def test_seconds_to_hms_zero(self):
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))

    def test_seconds_to_hms_one_second(self):
        self.assertEqual(seconds_to_hms(1), (0, 0, 1))

    def test_seconds_to_hms_one_minute(self):
        self.assertEqual(seconds_to_hms(60), (0, 1, 0))

    def test_seconds_to_hms_one_hour(self):
        self.assertEqual(seconds_to_hms(3600), (1, 0, 0))

    def test_seconds_to_hms_mixed_values(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))

    def test_seconds_to_hms_large_value(self):
        self.assertEqual(seconds_to_hms(86400), (24, 0, 0))

    def test_seconds_to_hms_negative_raises(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)

    def test_hms_to_seconds_zero(self):
        self.assertEqual(hms_to_seconds(0, 0, 0), 0)

    def test_hms_to_seconds_one_second(self):
        self.assertEqual(hms_to_seconds(0, 0, 1), 1)

    def test_hms_to_seconds_one_minute(self):
        self.assertEqual(hms_to_seconds(0, 1, 0), 60)

    def test_hms_to_seconds_one_hour(self):
        self.assertEqual(hms_to_seconds(1, 0, 0), 3600)

    def test_hms_to_seconds_mixed_values(self):
        self.assertEqual(hms_to_seconds(1, 1, 1), 3661)

    def test_hms_to_seconds_large_value(self):
        self.assertEqual(hms_to_seconds(24, 0, 0), 86400)

    def test_hms_to_seconds_negative_raises(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, -1, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, -1)

    def test_round_trip_conversion(self):
        total = 12345
        hours, minutes, seconds = seconds_to_hms(total)
        self.assertEqual(hms_to_seconds(hours, minutes, seconds), total)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)