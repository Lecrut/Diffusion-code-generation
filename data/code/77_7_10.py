import unittest

def time_to_minutes(hours: int, minutes: int) -> int:
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
    sample_hours_1 = 12
    sample_minutes_1 = 30
    result_1 = time_to_minutes(sample_hours_1, sample_minutes_1)
    print(result_1)

    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTimeToMinutes('test_zero_time'))
    test_suite.addTest(TestTimeToMinutes('test_max_time'))
    test_suite.addTest(TestTimeToMinutes('test_edge_cases'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)