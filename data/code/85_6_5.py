import unittest
from datetime import date
class TestDateDifference:
    def calculate_week_difference(self, date1, date2):
        diff = abs((date1 - date2).days)
        return diff
class TestWeekDifference(unittest.TestCase):
    def setUp(self):
        self.calculator = TestDateDifference()
    def test_same_week_difference(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 7)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 6)
    def test_different_weeks(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 8)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 7)
    def test_reverse_order(self):
        date1 = date(2023, 1, 8)
        date2 = date(2023, 1, 1)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 7)
    def test_month_boundary(self):
        date1 = date(2023, 1, 30)
        date2 = date(2023, 2, 2)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 2)
    def test_year_boundary(self):
        date1 = date(2023, 12, 31)
        date2 = date(2024, 1, 2)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 2)
    def test_large_difference(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 31)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 30)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)