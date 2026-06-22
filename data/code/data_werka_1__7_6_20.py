import unittest

def convert_seconds_to_minutes(seconds):
    return seconds // 60

def convert_minutes_to_hours(minutes):
    return minutes // 60

class TestTimeConversion(unittest.TestCase):

    def test_convert_seconds_to_minutes(self):
        self.assertEqual(convert_seconds_to_minutes(0), 0)
        self.assertEqual(convert_seconds_to_minutes(59), 0)
        self.assertEqual(convert_seconds_to_minutes(60), 1)
        self.assertEqual(convert_seconds_to_minutes(3600), 60)

    def test_convert_minutes_to_hours(self):
        self.assertEqual(convert_minutes_to_hours(0), 0)
        self.assertEqual(convert_minutes_to_hours(59), 0)
        self.assertEqual(convert_minutes_to_hours(60), 1)
        self.assertEqual(convert_minutes_to_hours(7200), 120)

if __name__ == '__main__':
    print("Testing time conversion functions...")
    unittest.main(argv=[''], exit=False)