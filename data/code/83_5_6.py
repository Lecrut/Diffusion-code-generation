import unittest
from datetime import date

def are_dates_equal(date1: date, date2: date) -> bool:
    return date1 == date2

class TestDateEquality(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(are_dates_equal(date(2023, 4, 1), date(2023, 4, 1)))

    def test_different_dates(self):
        self.assertFalse(are_dates_equal(date(2023, 4, 1), date(2023, 4, 2)))

    def test_edge_case_same_year_month_day(self):
        self.assertTrue(are_dates_equal(date(1900, 1, 1), date(1900, 1, 1)))

    def test_edge_case_different_year(self):
        self.assertFalse(are_dates_equal(date(1900, 1, 1), date(2000, 1, 1)))

    def test_edge_case_different_month(self):
        self.assertFalse(are_dates_equal(date(2023, 1, 1), date(2023, 2, 1)))

    def test_edge_case_different_day(self):
        self.assertFalse(are_dates_equal(date(2023, 4, 1), date(2023, 4, 30)))

if __name__ == '__main__':
    unittest.main()