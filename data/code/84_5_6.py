import unittest
from datetime import date
class DayOfYearCalculator:
    def calculate_day_of_year(self, year, month, day):
        if year < 1:
            raise ValueError("Year must be positive")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0:
            days_in_month[2] = 29
        day_of_year = 0
        for m in range(1, month):
            day_of_year += days_in_month[m]
        day_of_year += day
        return day_of_year
class TestDayOfYearCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DayOfYearCalculator()
    def test_standard_date(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 10, 26), 299)
    def test_start_of_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 1, 1), 1)
    def test_end_of_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 12, 31), 365)
    def test_non_leap_year(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 1), 32)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 28), 59)
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 3, 1), 60)
    def test_leap_year_february_29(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 1), 32)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 2, 29), 60)
        self.assertEqual(self.calculator.calculate_day_of_year(2024, 3, 1), 61)
    def test_non_leap_year_february_29_check(self):
        self.assertEqual(self.calculator.calculate_day_of_year(2023, 2, 29), 60)                                            
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)