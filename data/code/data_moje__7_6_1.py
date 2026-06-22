import unittest

def seconds_to_hms(total_seconds):
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be a number")
    if total_seconds < 0:
        raise ValueError("Input must be non-negative")
    
    total_seconds = int(total_seconds)
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return (hours, minutes, seconds)

def hms_to_seconds(hours, minutes, seconds):
    if not all(isinstance(x, (int, float)) for x in [hours, minutes, seconds]):
        raise TypeError("All inputs must be numbers")
    if any(x < 0 for x in [hours, minutes, seconds]):
        raise ValueError("All inputs must be non-negative")
    
    return hours * 3600 + minutes * 60 + seconds

class TestTimeConversion(unittest.TestCase):
    
    def test_seconds_to_hms_basic(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))
    
    def test_seconds_to_hms_zero(self):
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))
    
    def test_seconds_to_hms_large(self):
        self.assertEqual(seconds_to_hms(86400), (24, 0, 0))
    
    def test_seconds_to_hms_large_span(self):
        self.assertEqual(seconds_to_hms(1000000), (277, 46, 40))
    
    def test_seconds_to_hms_negative(self):
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)
    
    def test_seconds_to_hms_invalid_type(self):
        with self.assertRaises(TypeError):
            seconds_to_hms("abc")
    
    def test_hms_to_seconds_basic(self):
        self.assertEqual(hms_to_seconds(1, 1, 1), 3661)
    
    def test_hms_to_seconds_zero(self):
        self.assertEqual(hms_to_seconds(0, 0, 0), 0)
    
    def test_hms_to_seconds_large(self):
        self.assertEqual(hms_to_seconds(24, 0, 0), 86400)
    
    def test_hms_to_seconds_large_span(self):
        self.assertEqual(hms_to_seconds(277, 46, 40), 1000000)
    
    def test_hms_to_seconds_negative(self):
        with self.assertRaises(ValueError):
            hms_to_seconds(-1, 0, 0)
    
    def test_hms_to_seconds_invalid_type(self):
        with self.assertRaises(TypeError):
            hms_to_seconds("a", 0, 0)

if __name__ == '__main__':
    print(seconds_to_hms(3661))
    print(seconds_to_hms(0))
    print(seconds_to_hms(86400))
    print(hms_to_seconds(1, 1, 1))
    print(hms_to_seconds(0, 0, 0))
    print(hms_to_seconds(24, 0, 0))
    unittest.main()