import unittest
from datetime import date

def are_dates_equal(date1: date, date2: date) -> bool:
    return date1 == date2

class TestDateEquality(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(are_dates_equal(date(2023, 10, 1), date(2023, 10, 1)))

    def test_different_dates(self):
        self.assertFalse(are_dates_equal(date(2023, 10, 1), date(2023, 10, 2)))

    def test_edge_case_same_day_but_different_year(self):
        self.assertFalse(are_dates_equal(date(2022, 10, 1), date(2023, 10, 1)))

if __name__ == '__main__':
    unittest.main()