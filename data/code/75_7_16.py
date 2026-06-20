import unittest
from datetime import datetime

def date_difference(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    if date1 > date2:
        diff = date1 - date2
    else:
        diff = date2 - date1
    days = diff.days
    return days

class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        self.assertEqual(date_difference("2023-10-26", "2023-10-26"), 0)

    def test_future_date(self):
        self.assertEqual(date_difference("2023-10-27", "2023-10-26"), 1)

    def test_past_date(self):
        self.assertEqual(date_difference("2023-10-25", "2023-10-26"), -1)

if __name__ == '__main__':
    unittest.main()