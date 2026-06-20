import datetime
from unittest import TestCase, main

def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2

class TestDateComparison(TestCase):
    def test_identical_dates(self):
        date1 = datetime.date(2023, 10, 27)
        date2 = datetime.date(2023, 10, 27)
        self.assertTrue(are_dates_identical(date1, date2))

    def test_different_dates(self):
        date1 = datetime.date(2023, 10, 27)
        date2 = datetime.date(2023, 10, 28)
        self.assertFalse(are_dates_identical(date1, date2))

    def test_edge_case_same_year_month_day(self):
        date1 = datetime.date(2000, 1, 1)
        date2 = datetime.date(2000, 1, 1)
        self.assertTrue(are_dates_identical(date1, date2))

    def test_edge_case_different_year(self):
        date1 = datetime.date(2000, 1, 1)
        date2 = datetime.date(2001, 1, 1)
        self.assertFalse(are_dates_identical(date1, date2))

    def test_edge_case_different_month(self):
        date1 = datetime.date(2000, 1, 1)
        date2 = datetime.date(2000, 2, 1)
        self.assertFalse(are_dates_identical(date1, date2))

    def test_edge_case_different_day(self):
        date1 = datetime.date(2000, 1, 1)
        date2 = datetime.date(2000, 1, 2)
        self.assertFalse(are_dates_identical(date1, date2))

if __name__ == '__main__':
    main()