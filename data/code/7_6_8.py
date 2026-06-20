import unittest

def seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    total_seconds = int(total_seconds)
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds

def hms_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    if not (isinstance(hours, (int, float)) and isinstance(minutes, (int, float)) and isinstance(seconds, (int, float))):
        raise TypeError("Time components must be numeric")
    if minutes >= 60:
        raise ValueError("Minutes must be less than 60")
    if seconds >= 60:
        raise ValueError("Seconds must be less than 60")
    return hours * 3600 + minutes * 60 + seconds

def format_time(total_seconds):
    h, m, s = seconds_to_hms(total_seconds)
    return f"{h:02d}:{m:02d}:{s:02d}"

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_hms_zero(self):
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))

    def test_seconds_to_hms_one_second(self):
        self.assertEqual(seconds_to_hms(1), (0, 0, 1))

    def test_seconds_to_hms_one_minute(self):
        self.assertEqual(seconds_to_hms(60), (0, 1, 0))

    def test_seconds_to_hms_one_hour(self):
        self.assertEqual(seconds_to_hms(3600), (1, 0, 0))

    def test_seconds_to_hms_complex(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))

    def test_seconds_to_hms_large_span(self):
        total = 86400 * 30
        expected_hours = total // 3600
        self.assertEqual(seconds_to_hms(total)[0], expected_hours)

    def test_seconds_to_hms_negative(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)

    def test_hms_to_seconds_zero(self):
        self.assertEqual(hms_to_seconds(0, 0, 0), 0)

    def test_hms_to_seconds_one_hour(self):
        self.assertEqual(hms_to_seconds(1, 0, 0), 3600)

    def test_hms_to_seconds_one_minute(self):
        self.assertEqual(hms_to_seconds(0, 1, 0), 60)

    def test_hms_to_seconds_one_second(self):
        self.assertEqual(hms_to_seconds(0, 0, 1), 1)

    def test_hms_to_seconds_complex(self):
        self.assertEqual(hms_to_seconds(1, 1, 1), 3661)

    def test_hms_to_seconds_negative_hours(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)

    def test_hms_to_seconds_invalid_minutes(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 60, 0)

    def test_hms_to_seconds_invalid_seconds(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, 60)

    def test_hms_to_seconds_non_numeric(self):
        with self.assertRaises(TypeError):
            hms_to_seconds("1", 0, 0)

    def test_round_trip(self):
        h, m, s = 12, 30, 45
        total = hms_to_seconds(h, m, s)
        h2, m2, s2 = seconds_to_hms(total)
        self.assertEqual((h, m, s), (h2, m2, s2))

    def test_format_time_zero(self):
        self.assertEqual(format_time(0), "00:00:00")

    def test_format_time_one_second(self):
        self.assertEqual(format_time(1), "00:00:01")

    def test_format_time_large(self):
        self.assertEqual(format_time(3661), "01:01:01")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(seconds_to_hms(3661))
    print(hms_to_seconds(1, 1, 1))
    print(format_time(3661))