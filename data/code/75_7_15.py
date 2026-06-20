import datetime
import unittest

class DateDifferenceCalculator:
    def calculate_difference(self, date1_str: str, date2_str: str) -> tuple:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
        diff = abs(date1 - date2)
        total_seconds = int(diff.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds

class TestDateDifferenceCalculator(unittest.TestCase):
    def test_same_day(self):
        calculator = DateDifferenceCalculator()
        self.assertEqual(calculator.calculate_difference("2023-10-26 10:00:00", "2023-10-26 12:30:45"), (2, 30, 45))

    def test_future_date(self):
        calculator = DateDifferenceCalculator()
        self.assertEqual(calculator.calculate_difference("2023-10-27 10:00:00", "2023-10-26 12:30:45"), (1, 29, 14))

    def test_past_date(self):
        calculator = DateDifferenceCalculator()
        self.assertEqual(calculator.calculate_difference("2023-10-26 12:30:45", "2023-10-27 10:00:00"), (1, 29, 14))

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_difference("2023-10-26 10:00:00", "2023-10-26 12:30:45"))