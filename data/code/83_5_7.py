import unittest
from datetime import date

def dates_are_same(date1: date, date2: date) -> bool:
    return date1 == date2

class TestDatesAreSame(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(dates_are_same(date(2023, 10, 5), date(2023, 10, 5)))

    def test_different_dates(self):
        self.assertFalse(dates_are_same(date(2023, 10, 5), date(2023, 10, 6)))

    def test_edge_case_min_date(self):
        self.assertTrue(dates_are_same(date.min, date.min))

    def test_edge_case_max_date(self):
        self.assertTrue(dates_are_same(date.max, date.max))

if __name__ == '__main__':
    unittest.main()