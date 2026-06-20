import unittest

def time_to_minutes(hours: int, minutes: int) -> int:
    if not isinstance(hours, int) or not isinstance(minutes, int):
        raise ValueError("Both hours and minutes must be integers")
    if hours < 0 or minutes < 0:
        raise ValueError("Hours and minutes must be non-negative")
    if hours > 23 or (hours == 23 and minutes > 59):
        raise ValueError("Invalid time format")
    return hours * 60 + minutes

class TestTimeToMinutes(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(time_to_minutes(0, 0), 0)

    def test_max_time(self):
        self.assertEqual(time_to_minutes(23, 59), 1439)

    def test_edge_cases(self):
        self.assertEqual(time_to_minutes(1, 0), 60)
        self.assertEqual(time_to_minutes(0, 1), 1)
        self.assertEqual(time_to_minutes(1, 1), 61)

if __name__ == '__main__':
    unittest.main()