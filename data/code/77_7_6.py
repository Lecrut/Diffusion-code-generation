import unittest

class TimeConverter:
    MAX_HOURS = 23
    MAX_MINUTES = 59

    @staticmethod
    def time_to_minutes(hours: int, minutes: int) -> int:
        return hours * 60 + minutes

class TestTimeConverter(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(TimeConverter.time_to_minutes(0, 0), 0)

    def test_max_time(self):
        self.assertEqual(TimeConverter.time_to_minutes(TimeConverter.MAX_HOURS, TimeConverter.MAX_MINUTES), 1439)

if __name__ == '__main__':
    unittest.main()