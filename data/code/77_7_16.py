import unittest

class TimeConverter:
    MAX_HOURS = 23
    MAX_MINUTES = 59

    @staticmethod
    def time_to_minutes(hours: int, minutes: int) -> int:
        return hours * 60 + minutes

class TestTimeToMinutes(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(TimeConverter.time_to_minutes(0, 0), 0)

    def test_max_time(self):
        self.assertEqual(TimeConverter.time_to_minutes(TimeConverter.MAX_HOURS, TimeConverter.MAX_MINUTES), 1439)

if __name__ == '__main__':
    sample_hours_1 = 12
    sample_minutes_1 = 30
    result_1 = TimeConverter.time_to_minutes(sample_hours_1, sample_minutes_1)
    print(result_1)
    sample_hours_2 = 0
    sample_minutes_2 = 0
    result_2 = TimeConverter.time_to_minutes(sample_hours_2, sample_minutes_2)
    print(result_2)