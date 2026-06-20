import unittest
from datetime import datetime

def date_difference(date1_str, date2_str):
    format_str = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, format_str)
    date2 = datetime.strptime(date2_str, format_str)
    diff = abs(date1 - date2)
    return diff.days

class TestDateDifference(unittest.TestCase):

    def test_same_day(self):
        self.assertEqual(date_difference("2023-10-26", "2023-10-26"), 0)

    def test_future_date(self):
        self.assertEqual(date_difference("2024-01-01", "2023-12-31"), 1)

    def test_past_date(self):
        self.assertEqual(date_difference("2023-12-31", "2024-01-01"), -1)

if __name__ == '__main__':
    unittest.main()