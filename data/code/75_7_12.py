import datetime
import unittest

def time_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    
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
        date_a = "2023-10-27 10:00:00"
        date_b = "2023-10-27 14:30:00"
        expected = (4, 30, 0)
        self.assertEqual(time_difference(date_a, date_b), expected)

    def test_future_date(self):
        date_a = "2023-10-28 10:00:00"
        date_b = "2023-10-27 14:30:00"
        expected = (1, 26, 30)
        self.assertEqual(time_difference(date_a, date_b), expected)

    def test_past_date(self):
        date_a = "2023-10-27 14:30:00"
        date_b = "2023-10-28 10:00:00"
        expected = (1, 26, 30)
        self.assertEqual(time_difference(date_a, date_b), expected)

if __name__ == '__main__':
    unittest.main()