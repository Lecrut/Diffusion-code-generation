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
        start = "2023-01-01 10:00:00"
        end = "2023-01-03 14:30:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.days, 2)
        self.assertEqual(result.seconds, 282400)
    def test_same_time(self):
        start = "2023-01-01 10:00:00"
        end = "2023-01-01 10:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 0)
    def test_crossing_day_boundary(self):
        start = "2023-12-31 23:00:00"
        end = "2024-01-01 01:00:00"
        expected_diff = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        result = self.calculator.calculate_difference(start, end)
        self.assertEqual(result.total_seconds(), 3600)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)