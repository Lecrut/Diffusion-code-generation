import unittest
from datetime import date, timedelta
def get_next_month(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return date(next_year, next_month, 1)
class TestNextMonth(unittest.TestCase):
    def test_standard_month(self):
        self.assertEqual(get_next_month(2023, 1), date(2023, 2, 1))
        self.assertEqual(get_next_month(2023, 5), date(2023, 6, 1))
    def test_year_boundary(self):
        self.assertEqual(get_next_month(2023, 12), date(2024, 1, 1))
    def test_non_leap_year_boundary(self):
        self.assertEqual(get_next_month(2023, 12), date(2024, 1, 1))
    def test_leap_year_boundary(self):
        self.assertEqual(get_next_month(2024, 12), date(2025, 1, 1))
    def test_middle_of_year(self):
        self.assertEqual(get_next_month(2024, 6), date(2024, 7, 1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)