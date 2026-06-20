import unittest
from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

class TestDaysBetweenDates(unittest.TestCase):

    def test_same_day(self):
        self.assertEqual(days_between_dates(date(2023, 4, 1), date(2023, 4, 1)), 0)

    def test_future_date(self):
        self.assertEqual(days_between_dates(date(2023, 4, 1), date(2023, 4, 5)), 4)

    def test_past_date(self):
        self.assertEqual(days_between_dates(date(2023, 4, 5), date(2023, 4, 1)), 4)

if __name__ == '__main__':
    unittest.main()