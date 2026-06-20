import unittest

def convert_seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Time cannot be negative")
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be a number")
    hours = int(total_seconds) // 3600
    remaining_seconds = int(total_seconds) % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

def convert_hms_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    if not all(isinstance(x, (int, float)) for x in [hours, minutes, seconds]):
        raise TypeError("Time components must be numbers")
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

class TestTimeConversion(unittest.TestCase):
    
    def test_convert_seconds_to_hms_zero(self):
        result = convert_seconds_to_hms(0)
        self.assertEqual(result, (0, 0, 0))
    
    def test_convert_seconds_to_hms_one_hour(self):
        result = convert_seconds_to_hms(3600)
        self.assertEqual(result, (1, 0, 0))
    
    def test_convert_seconds_to_hms_one_minute(self):
        result = convert_seconds_to_hms(60)
        self.assertEqual(result, (0, 1, 0))
    
    def test_convert_seconds_to_hms_one_second(self):
        result = convert_seconds_to_hms(1)
        self.assertEqual(result, (0, 0, 1))
    
    def test_convert_seconds_to_hms_large_value(self):
        result = convert_seconds_to_hms(86400)
        self.assertEqual(result, (24, 0, 0))
    
    def test_convert_seconds_to_hms_mixed_values(self):
        result = convert_seconds_to_hms(3661)
        self.assertEqual(result, (1, 1, 1))
    
    def test_convert_seconds_to_hms_negative_value(self):
        with self.assertRaises(ValueError):
            convert_seconds_to_hms(-1)
    
    def test_convert_seconds_to_hms_invalid_type(self):
        with self.assertRaises(TypeError):
            convert_seconds_to_hms("abc")
    
    def test_convert_hms_to_seconds_zero(self):
        result = convert_hms_to_seconds(0, 0, 0)
        self.assertEqual(result, 0)
    
    def test_convert_hms_to_seconds_one_hour(self):
        result = convert_hms_to_seconds(1, 0, 0)
        self.assertEqual(result, 3600)
    
    def test_convert_hms_to_seconds_one_minute(self):
        result = convert_hms_to_seconds(0, 1, 0)
        self.assertEqual(result, 60)
    
    def test_convert_hms_to_seconds_one_second(self):
        result = convert_hms_to_seconds(0, 0, 1)
        self.assertEqual(result, 1)
    
    def test_convert_hms_to_seconds_mixed_values(self):
        result = convert_hms_to_seconds(1, 1, 1)
        self.assertEqual(result, 3661)
    
    def test_convert_hms_to_seconds_negative_value(self):
        with self.assertRaises(ValueError):
            convert_hms_to_seconds(-1, 0, 0)
    
    def test_convert_hms_to_seconds_negative_minutes(self):
        with self.assertRaises(ValueError):
            convert_hms_to_seconds(0, -1, 0)
    
    def test_convert_hms_to_seconds_negative_seconds(self):
        with self.assertRaises(ValueError):
            convert_hms_to_seconds(0, 0, -1)
    
    def test_convert_hms_to_seconds_invalid_type(self):
        with self.assertRaises(TypeError):
            convert_hms_to_seconds("1", 0, 0)
    
    def test_round_trip_conversion(self):
        original_hms = (10, 30, 45)
        seconds = convert_hms_to_seconds(*original_hms)
        result_hms = convert_seconds_to_hms(seconds)
        self.assertEqual(result_hms, original_hms)
    
    def test_large_time_span_conversion(self):
        original_hms = (1000000, 59, 59)
        seconds = convert_hms_to_seconds(*original_hms)
        result_hms = convert_seconds_to_hms(seconds)
        self.assertEqual(result_hms, original_hms)

if __name__ == '__main__':
    sample_tests = [
        (0, "Zero seconds"),
        (3600, "One hour"),
        (3661, "One hour one minute one second"),
        (86400, "One day"),
        (123456, "Random large value"),
    ]
    
    print("Time Conversion Results:")
    for total_sec, description in sample_tests:
        h, m, s = convert_seconds_to_hms(total_sec)
        print(f"{description}: {total_sec}s = {h}h {m}m {s}s")
    
    back_to_sec = convert_hms_to_seconds(h, m, s)
    print(f"Back to seconds: {back_to_sec}s")
    
    unittest.main(argv=[''], exit=False, verbosity=2)