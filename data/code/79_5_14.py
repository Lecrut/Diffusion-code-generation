import unittest
from datetime import date, timedelta

def next_month(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    try:
        return date(year, month, day)
    except ValueError:
        return date(year, month, 1)

class TestNextMonth(unittest.TestCase):

    def test_next_month(self):
        self.assertEqual(next_month(date(2023, 1, 15)), date(2023, 2, 15))
        self.assertEqual(next_month(date(2023, 12, 15)), date(2024, 1, 15))
        self.assertEqual(next_month(date(2023, 2, 28)), date(2023, 3, 28))
        self.assertEqual(next_month(date(2023, 2, 29)), date(2024, 3, 1))
        self.assertEqual(next_month(date(2023, 11, 30)), date(2023, 12, 30))
        self.assertEqual(next_month(date(2023, 12, 31)), date(2024, 1, 1))
if __name__ == '__main__':
    unittest.main()