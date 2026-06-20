import unittest

def time_to_minutes(hours: int, minutes: int) -> int:
    return hours * 60 + minutes

class TestTimeToMinutes(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(time_to_minutes(0, 0), 0)

    def test_max_hours(self):
        self.assertEqual(time_to_minutes(23, 59), 1439)

    def test_edge_cases(self):
        self.assertEqual(time_to_minutes(1, 0), 60)
        self.assertEqual(time_to_minutes(0, 1), 1)
        self.assertEqual(time_to_minutes(1, 1), 61)

if __name__ == '__main__':
    unittest.main()