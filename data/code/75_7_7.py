import unittest
from datetime import date

def days_between_dates(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

class TestDaysBetweenDates(unittest.TestCase):
    def test_same_day(self):
        self.assertEqual(days_between_dates(date(2023, 4, 1), date(2023, 4, 1)), 0)
    
    def test_future_date(self):
        self.assertEqual(days_between_dates(date(2023, 4, 1), date(2023, 4, 15)), 14)
    
    def test_past_date(self):
        self.assertEqual(days_between_dates(date(2023, 4, 15), date(2023, 4, 1)), 14)

if __name__ == '__main__':
    unittest.main()