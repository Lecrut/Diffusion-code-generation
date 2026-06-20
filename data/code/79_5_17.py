import unittest
from datetime import datetime, timedelta

def next_month(date):
    year = date.year
    month = date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return datetime(year, month, 1)

class TestNextMonth(unittest.TestCase):
    def test_next_month(self):
        self.assertEqual(next_month(datetime(2023, 1, 15)), datetime(2023, 2, 1))
        self.assertEqual(next_month(datetime(2023, 12, 25)), datetime(2024, 1, 1))

if __name__ == '__main__':
    unittest.main()