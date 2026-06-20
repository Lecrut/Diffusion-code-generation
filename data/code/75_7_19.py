import unittest
from datetime import datetime

def time_difference(date1_str, date2_str):
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

class TestTimeDifference(unittest.TestCase):
    def test_same_day(self):
        result = time_difference("2023-10-27 10:00:00", "2023-10-27 12:30:45")
        self.assertEqual(result, (2, 30, 45))

    def test_future_date(self):
        result = time_difference("2023-10-28 10:00:00", "2023-10-27 12:30:45")
        self.assertEqual(result, (1, 29, 14))

    def test_past_date(self):
        result = time_difference("2023-10-26 10:00:00", "2023-10-27 12:30:45")
        self.assertEqual(result, (1, 29, 45))

if __name__ == '__main__':
    unittest.main()