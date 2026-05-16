import unittest
from datetime import date
def date_difference(date1, date2):
    return date2 - date1
class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(0, 0, 0))
    def test_future_date(self):
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 10)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(9, 0, 0))
    def test_past_date(self):
        date1 = date(2023, 1, 10)
        date2 = date(2023, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(-9, 0, 0))
    def test_different_years(self):
        date1 = date(2022, 12, 31)
        date2 = date(2023, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(1, 0, 0))
    def test_large_difference(self):
        date1 = date(2020, 1, 1)
        date2 = date(2024, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(4, 0, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)