import unittest

def time_to_minutes(hours, minutes):
    return hours * 60 + minutes

class TestTimeToMinutes(unittest.TestCase):

    def test_zero_time(self):
        self.assertEqual(time_to_minutes(0, 0), 0)

    def test_max_time(self):
        self.assertEqual(time_to_minutes(23, 59), 1439)

if __name__ == '__main__':
    unittest.main()