import unittest
from datetime import date
class TestDateComparison(unittest.TestCase):
    def are_dates_equal(self, date1, date2):
        return date1 == date2
    def test_identical_dates(self):
        d1 = date(2023, 10, 26)
        d2 = date(2023, 10, 26)
        self.assertTrue(self.are_dates_equal(d1, d2))
    def test_different_dates(self):
        d1 = date(2023, 10, 26)
        d2 = date(2023, 10, 27)
        self.assertFalse(self.are_dates_equal(d1, d2))
    def test_different_years(self):
        d1 = date(2023, 1, 1)
        d2 = date(2024, 1, 1)
        self.assertFalse(self.are_dates_equal(d1, d2))
    def test_different_months(self):
        d1 = date(2023, 1, 1)
        d2 = date(2023, 2, 1)
        self.assertFalse(self.are_dates_equal(d1, d2))
    def test_different_days(self):
        d1 = date(2023, 10, 26)
        d2 = date(2023, 10, 27)
        self.assertFalse(self.are_dates_equal(d1, d2))
    def test_edge_case_same_month_different_year(self):
        d1 = date(2023, 10, 15)
        d2 = date(2024, 10, 15)
        self.assertFalse(self.are_dates_equal(d1, d2))
    def test_edge_case_leap_year(self):
        d1 = date(2024, 2, 29)
        d2 = date(2024, 2, 29)
        self.assertTrue(self.are_dates_equal(d1, d2))
    def test_edge_case_leap_day_vs_non_leap_day(self):
        d1 = date(2024, 2, 29)
        d2 = date(2024, 3, 1)
        self.assertFalse(self.are_dates_equal(d1, d2))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)