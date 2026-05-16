import unittest
from datetime import date
def compare_dates(date1, date2):
    if date1 == date2:
        return 0
    elif date1 < date2:
        return -1
    else:
        return 1
class TestDateComparison(unittest.TestCase):
    def test_identical_dates(self):
        date1 = date(2023, 10, 26)
        date2 = date(2023, 10, 26)
        self.assertEqual(compare_dates(date1, date2), 0)
    def test_date1_before_date2(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 2)
        self.assertEqual(compare_dates(date1, date2), -1)
    def test_date1_after_date2(self):
        date1 = date(2023, 1, 2)
        date2 = date(2023, 1, 1)
        self.assertEqual(compare_dates(date1, date2), 1)
    def test_dates_spanning_years(self):
        date1 = date(2022, 12, 31)
        date2 = date(2023, 1, 1)
        self.assertEqual(compare_dates(date1, date2), -1)
    def test_dates_spanning_months(self):
        date1 = date(2023, 5, 15)
        date2 = date(2023, 6, 1)
        self.assertEqual(compare_dates(date1, date2), -1)
    def test_dates_spanning_years_and_months(self):
        date1 = date(2022, 11, 30)
        date2 = date(2023, 1, 1)
        self.assertEqual(compare_dates(date1, date2), -1)
    def test_dates_spanning_years_and_months_reversed(self):
        date1 = date(2023, 1, 1)
        date2 = date(2022, 12, 31)
        self.assertEqual(compare_dates(date1, date2), 1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)