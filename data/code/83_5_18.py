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

    def test_edge_case_same_day_of_year(self):
        self.assertTrue(DateComparator.are_dates_identical(date(2024, 1, 1), date(2025, 1, 1)))

if __name__ == '__main__':
    comparator = DateComparator()
    print(comparator.are_dates_identical(date(2023, 10, 27), date(2023, 10, 27)))
    print(comparator.are_dates_identical(date(2023, 10, 27), date(2023, 10, 28)))
    print(comparator.are_dates_identical(date(2024, 1, 1), date(2025, 1, 1)))

    unittest.main()