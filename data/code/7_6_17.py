import unittest

def seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError('Time cannot be negative')
    hours = int(total_seconds) // 3600
    remaining_seconds = int(total_seconds) % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return (hours, minutes, seconds)

def hms_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError('Time components cannot be negative')
    if minutes >= 60 or seconds >= 60:
        raise ValueError('Minutes and seconds must be less than 60')
    return hours * 3600 + minutes * 60 + seconds

def format_time(total_seconds):
    hours, minutes, seconds = seconds_to_hms(total_seconds)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_hms_zero(self):
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))

    def test_seconds_to_hms_one_second(self):
        self.assertEqual(seconds_to_hms(1), (0, 0, 1))

    def test_seconds_to_hms_one_minute(self):
        self.assertEqual(seconds_to_hms(60), (0, 1, 0))

    def test_seconds_to_hms_one_hour(self):
        self.assertEqual(seconds_to_hms(3600), (1, 0, 0))

    def test_seconds_to_hms_complex_time(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))

    def test_seconds_to_hms_large_time(self):
        self.assertEqual(seconds_to_hms(100000), (27, 46, 40))

    def test_seconds_to_hms_negative_raises(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)

    def test_hms_to_seconds_zero(self):
        self.assertEqual(hms_to_seconds(0, 0, 0), 0)

    def test_hms_to_seconds_one_hour(self):
        self.assertEqual(hms_to_seconds(1, 0, 0), 3600)

    def test_hms_to_seconds_complex_time(self):
        self.assertEqual(hms_to_seconds(2, 30, 45), 9045)

    def test_hms_to_seconds_large_time(self):
        self.assertEqual(hms_to_seconds(100, 50, 30), 360330)

    def test_hms_to_seconds_negative_raises(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, -1, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, -1)

    def test_hms_to_seconds_invalid_minutes_raises(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 60, 0)

    def test_hms_to_seconds_invalid_seconds_raises(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, 60)

    def test_round_trip_conversion(self):
        test_cases = [0, 1, 60, 3600, 3661, 100000, 86400, 864000]
        for seconds in test_cases:
            h, m, s = seconds_to_hms(seconds)
            self.assertEqual(hms_to_seconds(h, m, s), seconds)

    def test_format_time_zero(self):
        self.assertEqual(format_time(0), '00:00:00')

    def test_format_time_one_second(self):
        self.assertEqual(format_time(1), '00:00:01')

    def test_format_time_one_hour(self):
        self.assertEqual(format_time(3600), '01:00:00')

    def test_format_time_complex_time(self):
        self.assertEqual(format_time(3661), '01:01:01')

    def test_format_time_large_time(self):
        self.assertEqual(format_time(100000), '27:46:40')
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
    print(seconds_to_hms(0))
    print(seconds_to_hms(3661))
    print(hms_to_seconds(2, 30, 45))
    print(format_time(86400))