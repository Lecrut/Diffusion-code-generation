import unittest
from datetime import date

def are_dates_identical(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of datetime.date")
    return date1 == date2

class TestAreDatesIdentical(unittest.TestCase):
    def test_identical_dates(self):
        self.assertTrue(are_dates_identical(date(2023, 10, 27), date(2023, 10, 27)))

    def test_different_dates(self):
        self.assertFalse(are_dates_identical(date(2023, 10, 27), date(2023, 10, 28)))

    def test_edge_case_same_day_of_year(self):
        self.assertTrue(are_dates_identical(date(2024, 1, 1), date(2025, 1, 1)))

    def test_edge_case_different_day_of_year(self):
        self.assertFalse(are_dates_identical(date(2023, 12, 31), date(2024, 1, 1)))

if __name__ == '__main__':
    unittest.main()