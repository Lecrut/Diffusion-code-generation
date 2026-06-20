import datetime
import unittest

def time_difference(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
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
        self.assertEqual(time_difference("2023-10-26 10:00:00", "2023-10-26 12:30:45"), (2, 30, 45))

    def test_future_date(self):
        self.assertEqual(time_difference("2023-10-27 10:00:00", "2023-10-26 12:30:45"), (1, 29, 15))

    def test_past_date(self):
        self.assertEqual(time_difference("2023-10-26 12:30:45", "2023-10-27 10:00:00"), (1, 29, 15))

if __name__ == '__main__':
    date_a = "2023-10-26 10:00:00"
    date_b = "2023-10-27 14:30:15"
    hours, minutes, seconds = time_difference(date_a, date_b)
    print(f"Date A: {date_a}")
    print(f"Time Difference: {hours}h {minutes}m {seconds}s")