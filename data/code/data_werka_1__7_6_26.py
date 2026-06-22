import unittest

def seconds_to_hours(seconds):
    return seconds / 3600

def hours_to_seconds(hours):
    return hours * 3600

class TestTimeConversion(unittest.TestCase):

    def test_seconds_to_hours(self):
        self.assertEqual(seconds_to_hours(0), 0)
        self.assertEqual(seconds_to_hours(3600), 1)
        self.assertEqual(seconds_to_hours(7200), 2)
        self.assertEqual(seconds_to_hours(3601), 1.0002777777777776)

    def test_hours_to_seconds(self):
        self.assertEqual(hours_to_seconds(0), 0)
        self.assertEqual(hours_to_seconds(1), 3600)
        self.assertEqual(hours_to_seconds(2), 7200)
        self.assertEqual(hours_to_seconds(1.5), 5400)
if __name__ == '__main__':
    print(seconds_to_hours(0))
    print(seconds_to_hours(3600))
    print(seconds_to_hours(7200))
    print(seconds_to_hours(3601))
    print(hours_to_seconds(0))
    print(hours_to_seconds(1))
    print(hours_to_seconds(2))
    print(hours_to_seconds(1.5))
    unittest.main(argv=[''], exit=False)