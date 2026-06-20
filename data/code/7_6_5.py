import unittest
from datetime import timedelta

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    negative = total_seconds < 0
    if negative:
        total_seconds = -total_seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minutes")
    if seconds > 0:
        parts.append(f"{seconds} seconds")
    
    if not parts:
        return "0 seconds"
    
    return " ".join(parts)

class TestTimeConversion(unittest.TestCase):
    
    def test_zero_seconds(self):
        td = timedelta(seconds=0)
        result = format_timedelta(td)
        self.assertEqual(result, "0 seconds")
    
    def test_single_second(self):
        td = timedelta(seconds=1)
        result = format_timedelta(td)
        self.assertEqual(result, "1 seconds")
    
    def test_single_minute(self):
        td = timedelta(minutes=1)
        result = format_timedelta(td)
        self.assertEqual(result, "1 minutes")
    
    def test_single_hour(self):
        td = timedelta(hours=1)
        result = format_timedelta(td)
        self.assertEqual(result, "1 hours")
    
    def test_single_day(self):
        td = timedelta(days=1)
        result = format_timedelta(td)
        self.assertEqual(result, "1 days")
    
    def test_complex_duration(self):
        td = timedelta(days=2, hours=3, minutes=4, seconds=5)
        result = format_timedelta(td)
        self.assertEqual(result, "2 days 3 hours 4 minutes 5 seconds")
    
    def test_negative_duration(self):
        td = timedelta(days=-1, hours=-1, minutes=-1, seconds=-1)
        result = format_timedelta(td)
        self.assertEqual(result, "1 days 1 hours 1 minutes 1 seconds")
    
    def test_large_days(self):
        td = timedelta(days=365)
        result = format_timedelta(td)
        self.assertEqual(result, "365 days")
    
    def test_mixed_units_truncation(self):
        td = timedelta(seconds=90061)
        result = format_timedelta(td)
        self.assertEqual(result, "1 days 1 hours 1 minutes 1 seconds")
    
    def test_large_seconds(self):
        td = timedelta(seconds=86400 * 1000)
        result = format_timedelta(td)
        self.assertEqual(result, "1000 days")

def run_main():
    td1 = timedelta(days=1, hours=2, minutes=3, seconds=4)
    td2 = timedelta(seconds=0)
    td3 = timedelta(days=-1)
    
    print(format_timedelta(td1))
    print(format_timedelta(td2))
    print(format_timedelta(td3))

if __name__ == '__main__':
    run_main()
    unittest.main(argv=[''], exit=False, verbosity=2)