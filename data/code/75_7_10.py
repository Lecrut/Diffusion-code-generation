import unittest
from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    if date1 > date2:
        diff = date1 - date2
    else:
        diff = date2 - date1

    total_seconds = int(diff.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return hours, minutes, seconds

class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        date_a = "2023-10-27 10:00:00"
        date_b = "2023-10-27 14:30:00"
        hours, minutes, seconds = calculate_date_difference(date_a, date_b)
        self.assertEqual((hours, minutes, seconds), (4, 30, 0))

    def test_future_date(self):
        date_a = "2023-10-27 14:30:00"
        date_b = "2023-10-27 10:00:00"
        hours, minutes, seconds = calculate_date_difference(date_a, date_b)
        self.assertEqual((hours, minutes, seconds), (4, 30, 0))

    def test_past_date(self):
        date_a = "2023-10-26 10:00:00"
        date_b = "2023-10-27 10:00:00"
        hours, minutes, seconds = calculate_date_difference(date_a, date_b)
        self.assertEqual((hours, minutes, seconds), (24, 0, 0))

if __name__ == '__main__':
    unittest.main()