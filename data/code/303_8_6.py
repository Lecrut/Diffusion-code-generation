import unittest
from datetime import datetime
class TimeCalculator:
    def calculate_difference(self, start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
        difference = end_time - start_time
        return difference
    def calculate_duration_in_seconds(self, start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
        difference = end_time - start_time
        return difference.total_seconds()
class TestTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = TimeCalculator()
    def test_calculate_difference_positive(self):
        start = "2023-01-01 10:00:00"
        end = "2023-01-01 10:05:00"
        difference = self.calculator.calculate_difference(start, end)
        self.assertEqual(difference.total_seconds(), 300)
    def test_calculate_difference_negative(self):
        start = "2023-01-01 10:05:00"
        end = "2023-01-01 10:00:00"
        difference = self.calculator.calculate_difference(start, end)
        self.assertEqual(difference.total_seconds(), -300)
    def test_calculate_duration_in_seconds(self):
        start = "2023-10-26 14:30:00"
        end = "2023-10-27 14:35:30"
        duration = self.calculator.calculate_duration_in_seconds(start, end)
        self.assertEqual(duration, 3330.0)
    def test_duration_across_day(self):
        start = "2023-12-31 23:00:00"
        end = "2024-01-01 01:00:00"
        duration = self.calculator.calculate_duration_in_seconds(start, end)
        self.assertEqual(duration, 3600.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)