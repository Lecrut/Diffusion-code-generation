import unittest

def seconds_to_hours_minutes_seconds(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds

def hours_minutes_seconds_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds must be less than 60")
    return (hours * 3600) + (minutes * 60) + seconds

class TestTimeConversion(unittest.TestCase):
    def test_zero_values(self):
        self.assertEqual(seconds_to_hours_minutes_seconds(0), (0, 0, 0))
        self.assertEqual(hours_minutes_seconds_to_seconds(0, 0, 0), 0)

    def test_large_time_span(self):
        hours, minutes, seconds = seconds_to_hours_minutes_seconds(86400)
        self.assertEqual(hours, 24)
        self.assertEqual(minutes, 0)
        self.assertEqual(seconds, 0)

        total = hours_minutes_seconds_to_seconds(24, 0, 0)
        self.assertEqual(total, 86400)

    def test_mixed_values(self):
        self.assertEqual(seconds_to_hours_minutes_seconds(3661), (1, 1, 1))
        self.assertEqual(hours_minutes_seconds_to_seconds(1, 1, 1), 3661)

    def test_invalid_negative_input_seconds(self):
        with self.assertRaises(ValueError):
            seconds_to_hours_minutes_seconds(-1)

    def test_invalid_large_minutes(self):
        with self.assertRaises(ValueError):
            hours_minutes_seconds_to_seconds(1, 60, 0)

    def test_invalid_large_seconds(self):
        with self.assertRaises(ValueError):
            hours_minutes_seconds_to_seconds(0, 0, 60)

    def test_exact_hour_boundary(self):
        self.assertEqual(seconds_to_hours_minutes_seconds(7200), (2, 0, 0))
        self.assertEqual(hours_minutes_seconds_to_seconds(2, 0, 0), 7200)

    def test_exact_minute_boundary(self):
        self.assertEqual(seconds_to_hours_minutes_seconds(120), (0, 2, 0))
        self.assertEqual(hours_minutes_seconds_to_seconds(0, 2, 0), 120)

if __name__ == '__main__':
    result_1 = seconds_to_hours_minutes_seconds(0)
    print(result_1)
    result_2 = seconds_to_hours_minutes_seconds(90061)
    print(result_2)
    result_3 = hours_minutes_seconds_to_seconds(10, 0, 0)
    print(result_3)
    result_4 = hours_minutes_seconds_to_seconds(0, 0, 5)
    print(result_4)
    unittest.main()