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
    def test_crossing_day(self):
        start = "2023-01-01 23:00:00"
        end = "2023-01-02 01:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 3600)
    def test_larger_difference(self):
        start = "2023-01-01 00:00:00"
        end = "2023-01-05 12:30:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.days, 4)
        self.assertEqual(result.seconds, 45000)
    def test_zero_difference(self):
        start = "2023-01-01 15:30:00"
        end = "2023-01-01 15:30:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)