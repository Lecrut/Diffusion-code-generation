import unittest
from datetime import datetime
class TimeCalculator:
    def calculate_difference(self, start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
        difference = end_time - start_time
        return difference
class TestTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = TimeCalculator()
    def test_simple_difference(self):
        start = "2023-01-01 10:00:00"
        end = "2023-01-01 11:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result, expected_diff)
    def test_multi_day_difference(self):
        start = "2023-01-01 00:00:00"
        end = "2023-01-03 00:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.days, 2)
        self.assertEqual(result.seconds, 0)
    def test_time_with_minutes_and_seconds(self):
        start = "2023-10-26 14:30:15"
        end = "2023-10-26 15:15:45"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 4590)
    def test_zero_difference(self):
        start = "2023-05-15 12:00:00"
        end = "2023-05-15 12:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)