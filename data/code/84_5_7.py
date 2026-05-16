import unittest
from datetime import date
class DayOfYearCalculator:
    def calculate_day_of_year(self, year, month, day):
        if month == 2:
            if self._is_leap(year):
                return day
            else:
                return 28 + day
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_of_year = sum(days_in_month[1:month]) + day
        return day_of_year
    def _is_leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
class TestDayOfYearCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DayOfYearCalculator()
    def test_standard_dates(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 3, 1), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 12, 31), 365)
    def test_non_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 1), 2)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 28), 28)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 3, 1), 30)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 12, 31), 365)
    def test_leap_day_in_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 29), 60)
    def test_leap_day_in_non_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 29), 57)          
    def test_leap_year_behavior(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 29), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 3, 1), 61)
    def test_century_rule(self):
        self.assertEqual(self.calculator.calculate_day_of_year(1900, 2, 29), 57)          
        self.assertEqual(self.calculator.calculate_day_of_year(2000, 2, 29), 60)          
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)