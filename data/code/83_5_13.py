import unittest
from datetime import date

class DateComparator:
    @staticmethod
    def are_dates_identical(date1: date, date2: date) -> bool:
        return date1 == date2

class TestDateComparator(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(DateComparator.are_dates_identical(date(2023, 10, 27), date(2023, 10, 27)))

    def test_different_dates(self):
        self.assertFalse(DateComparator.are_dates_identical(date(2023, 10, 27), date(2023, 10, 28)))

    def test_edge_case_same_year_month_day(self):
        self.assertTrue(DateComparator.are_dates_identical(date(2000, 1, 1), date(2000, 1, 1)))

    def test_edge_case_different_year(self):
        self.assertFalse(DateComparator.are_dates_identical(date(1999, 12, 31), date(2000, 1, 1)))

if __name__ == '__main__':
    unittest.main()