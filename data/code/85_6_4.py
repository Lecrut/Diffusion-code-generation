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
    def test_reverse_order(self):
        date1 = date(2023, 1, 7)
        date2 = date(2023, 1, 1)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 6)
    def test_spanning_month_boundary(self):
        date1 = date(2023, 1, 30)
        date2 = date(2023, 2, 2)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 2)
    def test_spanning_year_boundary(self):
        date1 = date(2023, 12, 28)
        date2 = date(2024, 1, 3)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 5)
    def test_large_difference(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 31)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 30)
    def test_same_day(self):
        date1 = date(2023, 5, 10)
        date2 = date(2023, 5, 10)
        self.assertEqual(self.calculator.calculate_week_difference(date1, date2), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)