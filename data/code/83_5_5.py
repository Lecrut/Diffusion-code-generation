import unittest
from datetime import date

def are_dates_identical(date1: date, date2: date) -> bool:
    return date1 == date2

class TestDateComparison(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(are_dates_identical(date(2023, 10, 27), date(2023, 10, 27)))

    def test_different_dates(self):
        self.assertFalse(are_dates_identical(date(2023, 10, 27), date(2023, 10, 28)))

    def test_edge_case_same_year_month_day(self):
        self.assertTrue(are_dates_identical(date(2000, 1, 1), date(2000, 1, 1)))

    def test_edge_case_different_year(self):
        self.assertFalse(are_dates_identical(date(2000, 1, 1), date(2001, 1, 1)))

    def test_edge_case_different_month(self):
        self.assertFalse(are_dates_identical(date(2000, 1, 1), date(2000, 2, 1)))

    def test_edge_case_different_day(self):
        self.assertFalse(are_dates_identical(date(2000, 1, 1), date(2000, 1, 2)))

if __name__ == '__main__':
    unittest.main()