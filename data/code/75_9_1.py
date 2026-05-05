import unittest
from datetime import date
def date_difference(date1, date2):
    return date2 - date1
class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        date1 = date(2023, 10, 26)
        date2 = date(2023, 10, 26)
        result = date_difference(date1, date2)
        self.assertEqual(result, date(0))
    def test_future_date(self):
        date1 = date(2023, 10, 26)
        date2 = date(2023, 11, 26)
        result = date_difference(date1, date2)
        self.assertEqual(result.year, 1)
        self.assertEqual(result.month, 11)
        self.assertEqual(result.day, 26)
    def test_past_date(self):
        date1 = date(2023, 11, 26)
        date2 = date(2023, 10, 26)
        result = date_difference(date1, date2)
        self.assertEqual(result.year, -1)
        self.assertEqual(result.month, -10)
        self.assertEqual(result.day, 0)
    def test_crossing_year(self):
        date1 = date(2023, 12, 31)
        date2 = date(2024, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result.days, 1)
    def test_larger_difference(self):
        date1 = date(2020, 1, 1)
        date2 = date(2024, 1, 1)
        result = date_difference(date1, date2)
        self.assertEqual(result.days, 1461)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)