import unittest
from datetime import date

def date_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        self.assertEqual(date_difference(date(2023, 4, 1), date(2023, 4, 1)), 0)
    
    def test_future_date(self):
        self.assertEqual(date_difference(date(2023, 4, 1), date(2023, 4, 5)), 4)
    
    def test_past_date(self):
        self.assertEqual(date_difference(date(2023, 4, 5), date(2023, 4, 1)), 4)

if __name__ == '__main__':
    unittest.main()