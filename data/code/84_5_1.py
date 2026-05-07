import unittest
from datetime import date
class DayOfYearCalculator:
    def calculate_day_of_year(self, year, month, day):
        if year < 1:
            raise ValueError("Year must be a positive integer")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
        day_of_year = 0
        for m in range(1, month):
            day_of_year += days_in_month[m]
        day_of_year += day
        return day_of_year
class TestDayOfYearCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DayOfYearCalculator()
    def test_standard_dates(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 12, 31), 365)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 1, 1), 1)
    def test_non_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 1), 2)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 28), 59)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 3, 1), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 12, 31), 365)
    def test_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 1), 2)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 28), 59)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 29), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 3, 1), 61)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 12, 31), 366)
    def test_century_non_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(1900, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(1900, 2, 1), 31)
        self.assertEqual(self.calculator.calculate_day_of_year(1900, 3, 1), 32)
    def test_century_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2000, 2, 29), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2000, 3, 1), 61)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)