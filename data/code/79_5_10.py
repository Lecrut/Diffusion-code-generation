import unittest
from datetime import date, timedelta

def next_month(date):
    year = date.year
    month = date.month
    day = date.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    try:
        return date(year, month, day)
    except ValueError:
        return date(year, month, 1) - timedelta(days=1)

class TestNextMonth(unittest.TestCase):

    def test_next_month(self):
        self.assertEqual(next_month(date(2023, 1, 31)), date(2023, 2, 28))
        self.assertEqual(next_month(date(2023, 2, 28)), date(2023, 3, 31))
        self.assertEqual(next_month(date(2023, 4, 30)), date(2023, 5, 31))
        self.assertEqual(next_month(date(2023, 9, 30)), date(2023, 10, 31))
        self.assertEqual(next_month(date(2023, 11, 30)), date(2023, 12, 31))
        self.assertEqual(next_month(date(2023, 12, 31)), date(2024, 1, 31))
if __name__ == '__main__':
    unittest.main()