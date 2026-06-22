import unittest

def seconds_to_time(total_seconds):
    if total_seconds < 0:
        raise ValueError("Time cannot be negative")
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return days, hours, minutes, seconds

def time_to_seconds(days, hours, minutes, seconds):
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    if hours >= 24 or minutes >= 60 or seconds >= 60:
        raise ValueError("Time components out of range")
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

class TestTimeConversion(unittest.TestCase):
    def test_zero_seconds(self):
        self.assertEqual(seconds_to_time(0), (0, 0, 0, 0))

    def test_negative_seconds_raises(self):
        with self.assertRaises(ValueError):
            seconds_to_time(-1)

    def test_simple_conversion(self):
        self.assertEqual(seconds_to_time(3661), (0, 1, 1, 1))

    def test_day_boundary(self):
        self.assertEqual(seconds_to_time(86400), (1, 0, 0, 0))

    def test_large_time_span(self):
        self.assertEqual(seconds_to_time(999999999), (11574, 1, 46, 39))

    def test_time_to_seconds_zero(self):
        self.assertEqual(time_to_seconds(0, 0, 0, 0), 0)

    def test_time_to_seconds_valid(self):
        self.assertEqual(time_to_seconds(1, 2, 3, 4), 93784)

    def test_time_to_seconds_invalid_hours(self):
        with self.assertRaises(ValueError):
            time_to_seconds(0, 24, 0, 0)

    def test_time_to_seconds_invalid_minutes(self):
        with self.assertRaises(ValueError):
            time_to_seconds(0, 0, 60, 0)

    def test_time_to_seconds_invalid_seconds(self):
        with self.assertRaises(ValueError):
            time_to_seconds(0, 0, 0, 60)

    def test_round_trip_large(self):
        total = 1234567890
        days, hours, minutes, seconds = seconds_to_time(total)
        self.assertEqual(time_to_seconds(days, hours, minutes, seconds), total)

if __name__ == '__main__':
    result = seconds_to_time(3661)
    print(result)
    result = time_to_seconds(1, 1, 1, 1)
    print(result)
    result = seconds_to_time(8640000)
    print(result)
    unittest.main()