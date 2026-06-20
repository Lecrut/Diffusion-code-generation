import unittest
from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    if date1 > date2:
        difference = date1 - date2
    else:
        difference = date2 - date1
    
    total_seconds = int(difference.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

class TestDateDifference(unittest.TestCase):
    def test_same_day(self):
        self.assertEqual(calculate_date_difference("2023-10-27 10:00:00", "2023-10-27 12:30:45"), (2, 30, 45))
    
    def test_future_date(self):
        self.assertEqual(calculate_date_difference("2023-10-28 14:30:15", "2023-10-27 10:00:00"), (26, 30, 15))
    
    def test_past_date(self):
        self.assertEqual(calculate_date_difference("2023-10-27 10:00:00", "2023-10-28 14:30:15"), (26, 30, 15))

if __name__ == '__main__':
    date_a = "2023-10-27 10:00:00"
    date_b = "2023-10-28 14:30:15"
    h, m, s = calculate_date_difference(date_a, date_b)
    print(f"Date Difference: {h} hours, {m} minutes, {s} seconds")