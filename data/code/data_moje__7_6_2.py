import unittest

def seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    hours = int(total_seconds) // 3600
    remainder = int(total_seconds) % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return (hours, minutes, seconds)

def hms_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds must be less than 60")
    return hours * 3600 + minutes * 60 + seconds

def format_hms(hours, minutes, seconds):
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def parse_hms(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in HH:MM:SS format")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return (hours, minutes, seconds)

class TestTimeConversions(unittest.TestCase):
    def test_seconds_to_hms_zero(self):
        result = seconds_to_hms(0)
        self.assertEqual(result, (0, 0, 0))

    def test_seconds_to_hms_exact_hours(self):
        result = seconds_to_hms(3600)
        self.assertEqual(result, (1, 0, 0))

    def test_seconds_to_hms_exact_minutes(self):
        result = seconds_to_hms(60)
        self.assertEqual(result, (0, 1, 0))

    def test_seconds_to_hms_exact_seconds(self):
        result = seconds_to_hms(45)
        self.assertEqual(result, (0, 0, 45))

    def test_seconds_to_hms_combined(self):
        result = seconds_to_hms(3661)
        self.assertEqual(result, (1, 1, 1))

    def test_seconds_to_hms_large_value(self):
        result = seconds_to_hms(86400)
        self.assertEqual(result, (24, 0, 0))

    def test_seconds_to_hms_negative(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)

    def test_seconds_to_hms_fractional(self):
        result = seconds_to_hms(3661.9)
        self.assertEqual(result, (1, 1, 1))

    def test_hms_to_seconds_zero(self):
        result = hms_to_seconds(0, 0, 0)
        self.assertEqual(result, 0)

    def test_hms_to_seconds_hours(self):
        result = hms_to_seconds(1, 0, 0)
        self.assertEqual(result, 3600)

    def test_hms_to_seconds_combined(self):
        result = hms_to_seconds(1, 1, 1)
        self.assertEqual(result, 3661)

    def test_hms_to_seconds_negative_hours(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)

    def test_hms_to_seconds_negative_minutes(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, -1, 0)

    def test_hms_to_seconds_invalid_minutes(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 60, 0)

    def test_hms_to_seconds_invalid_seconds(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, 60)

    def test_format_hms_simple(self):
        result = format_hms(1, 2, 3)
        self.assertEqual(result, "01:02:03")

    def test_format_hms_single_digits(self):
        result = format_hms(0, 0, 0)
        self.assertEqual(result, "00:00:00")

    def test_format_hms_large_values(self):
        result = format_hms(99, 59, 59)
        self.assertEqual(result, "99:59:59")

    def test_parse_hms_valid(self):
        result = parse_hms("01:02:03")
        self.assertEqual(result, (1, 2, 3))

    def test_parse_hms_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_hms("1:2")

    def test_parse_hms_with_leading_zeros(self):
        result = parse_hms("00:00:00")
        self.assertEqual(result, (0, 0, 0))

    def test_round_trip_conversion(self):
        original_seconds = 12345
        hms = seconds_to_hms(original_seconds)
        converted_seconds = hms_to_seconds(*hms)
        self.assertEqual(converted_seconds, original_seconds)

    def test_round_trip_large_span(self):
        original_seconds = 1000000
        hms = seconds_to_hms(original_seconds)
        converted_seconds = hms_to_seconds(*hms)
        self.assertEqual(converted_seconds, original_seconds)

if __name__ == '__main__':
    test = unittest.TestLoader().loadTestsFromTestCase(TestTimeConversions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test)
    print(result)