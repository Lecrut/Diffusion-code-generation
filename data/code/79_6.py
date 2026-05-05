import unittest
from datetime import date
import calendar
def get_next_month(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return date(next_year, next_month)
class TestNextMonth(unittest.TestCase):
    def test_normal_month_transition(self):
        self.assertEqual(get_next_month(2023, 1), date(2023, 2))
        self.assertEqual(get_next_month(2023, 3), date(2023, 4))
        self.assertEqual(get_next_month(2023, 10), date(2023, 11))
    def test_year_boundary(self):
        self.assertEqual(get_next_month(2023, 12), date(2024, 1))
    def test_different_years(self):
        self.assertEqual(get_next_month(2022, 11), date(2022, 12))
        self.assertEqual(get_next_month(2024, 1), date(2024, 2))
    def test_leap_year_boundary(self):
        self.assertEqual(get_next_month(2024, 12), date(2025, 1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)