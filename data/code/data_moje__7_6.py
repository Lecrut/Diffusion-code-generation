import unittest

def seconds_to_hms(total_seconds):
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Total seconds must be a number")
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    
    hours = int(total_seconds // 3600)
    remaining = total_seconds % 3600
    minutes = int(remaining // 60)
    seconds = remaining % 60
    
    return hours, minutes, int(seconds)

def hms_to_seconds(hours, minutes, seconds):
    if not all(isinstance(x, (int, float)) for x in [hours, minutes, seconds]):
        raise TypeError("Hours, minutes, and seconds must be numbers")
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Hours, minutes, and seconds cannot be negative")
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return int(total_seconds)

class TestTimeConversion(unittest.TestCase):
    
    def test_zero_values(self):
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))
        self.assertEqual(hms_to_seconds(0, 0, 0), 0)
    
    def test_basic_conversion(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))
        self.assertEqual(hms_to_seconds(1, 1, 1), 3661)
    
    def test_large_time_span(self):
        hours = 24 * 365
        minutes = 0
        seconds = 0
        total = hms_to_seconds(hours, minutes, seconds)
        back = seconds_to_hms(total)
        self.assertEqual(back, (hours, minutes, seconds))
    
    def test_seconds_overflow(self):
        self.assertEqual(seconds_to_hms(70), (0, 1, 10))
        self.assertEqual(seconds_to_hms(3665), (1, 1, 5))
    
    def test_minutes_overflow(self):
        self.assertEqual(seconds_to_hms(3660), (1, 1, 0))
        self.assertEqual(hms_to_seconds(0, 61, 0), 3660)
    
    def test_invalid_negative_input_seconds(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-10)
    
    def test_invalid_negative_input_hms(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, -1, 0)
        with self.assertRaises(ValueError):
            hms_to_seconds(0, 0, -1)
    
    def test_invalid_type_input(self):
        with self.assertRaises(TypeError):
            seconds_to_hms("100")
        with self.assertRaises(TypeError):
            hms_to_seconds("1", "0", "0")

if __name__ == '__main__':
    print(seconds_to_hms(0))
    print(seconds_to_hms(3661))
    print(seconds_to_hms(86400 * 2))
    print(hms_to_seconds(0, 0, 0))
    print(hms_to_seconds(24, 0, 0))
    print(hms_to_seconds(1, 30, 45))
    unittest.main(argv=[''], exit=False, verbosity=2)