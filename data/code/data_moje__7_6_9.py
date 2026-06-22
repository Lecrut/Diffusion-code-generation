import unittest
from datetime import timedelta, datetime

def minutes_to_seconds(minutes: float) -> float:
    return minutes * 60

def hours_to_seconds(hours: float) -> float:
    return hours * 3600

def days_to_seconds(days: float) -> float:
    return days * 86400

def seconds_to_minutes(seconds: float) -> float:
    return seconds / 60

def seconds_to_hours(seconds: float) -> float:
    return seconds / 3600

def seconds_to_days(seconds: float) -> float:
    return seconds / 86400

def convert_time_span(seconds: float) -> dict:
    if seconds < 0:
        raise ValueError('Time span cannot be negative')
    days = int(seconds // 86400)
    remainder = seconds % 86400
    hours = int(remainder // 3600)
    remainder = remainder % 3600
    minutes = int(remainder // 60)
    secs = remainder % 60
    return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': secs, 'total_seconds': seconds}

def format_time_span(seconds: float) -> str:
    result = convert_time_span(seconds)
    parts = []
    if result['days'] > 0:
        parts.append(f"{result['days']}d")
    if result['hours'] > 0:
        parts.append(f"{result['hours']}h")
    if result['minutes'] > 0:
        parts.append(f"{result['minutes']}m")
    if result['seconds'] > 0 or not parts:
        parts.append(f"{result['seconds']}s")
    return ' '.join(parts)

class TestTimeConversionFunctions(unittest.TestCase):

    def test_minutes_to_seconds_zero(self):
        self.assertEqual(minutes_to_seconds(0), 0)

    def test_minutes_to_seconds_positive(self):
        self.assertEqual(minutes_to_seconds(10), 600)

    def test_minutes_to_seconds_float(self):
        self.assertEqual(minutes_to_seconds(1.5), 90.0)

    def test_hours_to_seconds_zero(self):
        self.assertEqual(hours_to_seconds(0), 0)

    def test_hours_to_seconds_positive(self):
        self.assertEqual(hours_to_seconds(2), 7200)

    def test_hours_to_seconds_float(self):
        self.assertEqual(hours_to_seconds(0.5), 1800.0)

    def test_days_to_seconds_zero(self):
        self.assertEqual(days_to_seconds(0), 0)

    def test_days_to_seconds_positive(self):
        self.assertEqual(days_to_seconds(1), 86400)

    def test_days_to_seconds_large(self):
        self.assertEqual(days_to_seconds(365), 31536000)

    def test_seconds_to_minutes_zero(self):
        self.assertEqual(seconds_to_minutes(0), 0)

    def test_seconds_to_minutes_positive(self):
        self.assertEqual(seconds_to_minutes(60), 1.0)

    def test_seconds_to_minutes_float(self):
        self.assertAlmostEqual(seconds_to_minutes(90), 1.5)

    def test_seconds_to_hours_zero(self):
        self.assertEqual(seconds_to_hours(0), 0)

    def test_seconds_to_hours_positive(self):
        self.assertEqual(seconds_to_hours(3600), 1.0)

    def test_seconds_to_hours_large(self):
        self.assertEqual(seconds_to_hours(7200), 2.0)

    def test_seconds_to_days_zero(self):
        self.assertEqual(seconds_to_days(0), 0)

    def test_seconds_to_days_positive(self):
        self.assertEqual(seconds_to_days(86400), 1.0)

    def test_seconds_to_days_large(self):
        self.assertEqual(seconds_to_days(172800), 2.0)

    def test_convert_time_span_zero(self):
        result = convert_time_span(0)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 0)
        self.assertEqual(result['minutes'], 0)
        self.assertEqual(result['seconds'], 0)
        self.assertEqual(result['total_seconds'], 0)

    def test_convert_time_span_positive(self):
        result = convert_time_span(3661)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 1)
        self.assertEqual(result['minutes'], 1)
        self.assertEqual(result['seconds'], 1)

    def test_convert_time_span_large_days(self):
        result = convert_time_span(86400)
        self.assertEqual(result['days'], 1)
        self.assertEqual(result['hours'], 0)
        self.assertEqual(result['minutes'], 0)
        self.assertEqual(result['seconds'], 0)

    def test_convert_time_span_negative_raises(self):
        with self.assertRaises(ValueError):
            convert_time_span(-10)

    def test_convert_time_span_max_int(self):
        large_seconds = 2 ** 31 - 1
        result = convert_time_span(large_seconds)
        self.assertEqual(result['total_seconds'], large_seconds)
        self.assertGreater(result['days'], 0)

    def test_convert_time_span_fractions(self):
        result = convert_time_span(90.5)
        self.assertEqual(result['days'], 0)
        self.assertEqual(result['hours'], 0)
        self.assertEqual(result['minutes'], 1)
        self.assertAlmostEqual(result['seconds'], 30.5)

    def test_format_time_span_zero(self):
        self.assertEqual(format_time_span(0), '0s')

    def test_format_time_span_positive(self):
        result = format_time_span(3661)
        self.assertEqual(result, '1h 1m 1s')

    def test_format_time_span_days(self):
        result = format_time_span(90061)
        self.assertEqual(result, '1d 1h 1m 1s')

    def test_format_time_span_only_hours(self):
        result = format_time_span(7200)
        self.assertEqual(result, '2h')

    def test_format_time_span_only_minutes(self):
        result = format_time_span(120)
        self.assertEqual(result, '2m')

    def test_format_time_span_large_days(self):
        result = format_time_span(86400)
        self.assertEqual(result, '1d')
if __name__ == '__main__':
    test_instance = convert_time_span(3661)
    formatted = format_time_span(3661)
    print(f'Converted: {test_instance}')
    print(f'Formatted: {formatted}')
    result_large = convert_time_span(86400)
    formatted_large = format_time_span(86400)
    print(f'Large Converted: {result_large}')
    print(f'Large Formatted: {formatted_large}')