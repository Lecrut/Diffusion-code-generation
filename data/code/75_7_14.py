import unittest
from datetime import datetime

def time_difference(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD HH:MM:SS") from e
    
    if date1 == date2:
        return 0, 0, 0
    elif date1 > date2:
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
        self.assertEqual(time_difference("2023-10-27 10:00:00", "2023-10-26 12:30:45"), (2, 30, 45))

    def test_past_date(self):
        self.assertEqual(time_difference("2023-10-26 12:30:45", "2023-10-27 10:00:00"), (2, 30, 45))

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError) as context:
            time_difference("2023-10-26", "2023-10-27 12:30:45")
        self.assertIn("Invalid date format", str(context.exception))

if __name__ == '__main__':
    unittest.main()