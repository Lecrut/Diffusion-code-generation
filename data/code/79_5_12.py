import unittest
from datetime import datetime, timedelta

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
        return datetime(year, month, day)
    except ValueError:
        return datetime(year, month, 1)

class TestNextMonth(unittest.TestCase):

    def test_next_month(self):
        self.assertEqual(next_month(datetime(2023, 1, 15)), datetime(2023, 2, 15))
        self.assertEqual(next_month(datetime(2023, 12, 25)), datetime(2024, 1, 25))
        self.assertEqual(next_month(datetime(2023, 2, 28)), datetime(2023, 3, 28))
        self.assertEqual(next_month(datetime(2023, 2, 29)), datetime(2024, 3, 1))
        self.assertEqual(next_month(datetime(2023, 11, 30)), datetime(2023, 12, 30))
        self.assertEqual(next_month(datetime(2023, 12, 31)), datetime(2024, 1, 1))
if __name__ == '__main__':
    unittest.main()