import unittest

def convert_seconds_to_hms(total_seconds):
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be a number")
    if total_seconds < 0:
        raise ValueError("Time cannot be negative")
    total_seconds = int(total_seconds)
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return (hours, minutes, seconds)

def convert_hms_to_seconds(hours, minutes, seconds):
    if not all(isinstance(x, (int, float)) for x in [hours, minutes, seconds]):
        raise TypeError("All inputs must be numbers")
    if any(x < 0 for x in [hours, minutes, seconds]):
        raise ValueError("Time components cannot be negative")
    return int(hours * 3600 + minutes * 60 + seconds)

class TestTimeConversion(unittest.TestCase):
    def test_convert_seconds_to_hms_zero(self):
        self.assertEqual(convert_seconds_to_hms(0), (0, 0, 0))
    
    def test_convert_seconds_to_hms_positive(self):
        self.assertEqual(convert_seconds_to_hms(3661), (1, 1, 1))
    
    def test_convert_seconds_to_hms_large(self):
        self.assertEqual(convert_seconds_to_hms(86400), (24, 0, 0))
    
    def test_convert_seconds_to_hms_negative(self):
        with self.assertRaises(ValueError):
            convert_seconds_to_hms(-1)
    
    def test_convert_seconds_to_hms_non_numeric(self):
        with self.assertRaises(TypeError):
            convert_seconds_to_hms("abc")
    
    def test_convert_hms_to_seconds_zero(self):
        self.assertEqual(convert_hms_to_seconds(0, 0, 0), 0)
    
    def test_convert_hms_to_seconds_positive(self):
        self.assertEqual(convert_hms_to_seconds(1, 1, 1), 3661)
    
    def test_convert_hms_to_seconds_large(self):
        self.assertEqual(convert_hms_to_seconds(24, 0, 0), 86400)
    
    def test_convert_hms_to_seconds_negative(self):
        with self.assertRaises(ValueError):
            convert_hms_to_seconds(-1, 0, 0)
    
    def test_convert_hms_to_seconds_non_numeric(self):
        with self.assertRaises(TypeError):
            convert_hms_to_seconds("a", 0, 0)

if __name__ == '__main__':
    unittest.main()
    print(convert_seconds_to_hms(3661))
    print(convert_hms_to_seconds(1, 1, 1))
    print(convert_seconds_to_hms(0))
    print(convert_hms_to_seconds(0, 0, 0))
    print(convert_seconds_to_hms(86400))
    print(convert_hms_to_seconds(24, 0, 0))