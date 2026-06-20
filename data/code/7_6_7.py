import unittest

def seconds_to_days_hours_minutes_seconds(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return (days, hours, minutes, seconds)

def days_hours_minutes_seconds_to_seconds(days, hours, minutes, seconds):
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    if hours > 23 or minutes > 59 or seconds > 59:
        raise ValueError("Invalid time components: hours must be < 24, minutes and seconds < 60")
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

class TestTimeConversion(unittest.TestCase):
    def test_zero_seconds(self):
        result = seconds_to_days_hours_minutes_seconds(0)
        self.assertEqual(result, (0, 0, 0, 0))

    def test_small_seconds(self):
        result = seconds_to_days_hours_minutes_seconds(90)
        self.assertEqual(result, (0, 0, 1, 30))

    def test_exactly_one_hour(self):
        result = seconds_to_days_hours_minutes_seconds(3600)
        self.assertEqual(result, (0, 1, 0, 0))

    def test_exactly_one_day(self):
        result = seconds_to_days_hours_minutes_seconds(86400)
        self.assertEqual(result, (1, 0, 0, 0))

    def test_large_time_span(self):
        result = seconds_to_days_hours_minutes_seconds(999999999)
        self.assertEqual(result, (11574, 1, 46, 39))

    def test_negative_seconds_raises(self):
        with self.assertRaises(ValueError):
            seconds_to_days_hours_minutes_seconds(-1)

    def test_round_trip_conversion(self):
        original_days, original_hours, original_minutes, original_seconds = 5, 10, 30, 45
        total = days_hours_minutes_seconds_to_seconds(original_days, original_hours, original_minutes, original_seconds)
        result = seconds_to_days_hours_minutes_seconds(total)
        self.assertEqual(result, (original_days, original_hours, original_minutes, original_seconds))

    def test_invalid_hours_raises(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_seconds_to_seconds(1, 24, 0, 0)

    def test_invalid_minutes_raises(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_seconds_to_seconds(1, 0, 60, 0)

    def test_invalid_seconds_raises(self):
        with self.assertRaises(ValueError):
            days_hours_minutes_seconds_to_seconds(1, 0, 0, 60)

    def test_zero_components(self):
        result = days_hours_minutes_seconds_to_seconds(0, 0, 0, 0)
        self.assertEqual(result, 0)

    def test_max_valid_components(self):
        result = days_hours_minutes_seconds_to_seconds(1, 23, 59, 59)
        expected = 1 * 86400 + 23 * 3600 + 59 * 60 + 59
        self.assertEqual(result, expected)

if __name__ == '__main__':
    test_obj = TestTimeConversion()
    test_obj.test_zero_seconds()
    test_obj.test_small_seconds()
    test_obj.test_exactly_one_hour()
    test_obj.test_exactly_one_day()
    test_obj.test_large_time_span()
    test_obj.test_round_trip_conversion()
    print(seconds_to_days_hours_minutes_seconds(999999999))
    print(days_hours_minutes_seconds_to_seconds(11574, 1, 46, 39))
    unittest.main(argv=[''], exit=False, verbosity=2)