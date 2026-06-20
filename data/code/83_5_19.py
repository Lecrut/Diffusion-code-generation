import unittest
from datetime import date

def dates_are_equal(date1: date, date2: date) -> bool:
    return date1 == date2

class TestDatesAreEqual(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(dates_are_equal(date(2023, 1, 1), date(2023, 1, 1)))

    def test_different_dates(self):
        self.assertFalse(dates_are_equal(date(2023, 1, 1), date(2023, 1, 2)))

    def test_edge_case_same_month_year(self):
        self.assertTrue(dates_are_equal(date(2023, 1, 15), date(2023, 1, 15)))

    def test_edge_case_different_months(self):
        self.assertFalse(dates_are_equal(date(2023, 1, 15), date(2023, 2, 15)))

    def test_edge_case_different_years(self):
        self.assertFalse(dates_are_equal(date(2023, 1, 15), date(2024, 1, 15)))

if __name__ == '__main__':
    unittest.main()