import unittest
def days_remaining(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month[2] = 29
    return 31 - days_in_month[month]
class TestDaysRemaining(unittest.TestCase):
    def test_standard_months(self):
        self.assertEqual(days_remaining(2023, 1), 30)
        self.assertEqual(days_remaining(2023, 2), 29)
        self.assertEqual(days_remaining(2023, 3), 28)
        self.assertEqual(days_remaining(2023, 4), 31)
        self.assertEqual(days_remaining(2023, 5), 30)
        self.assertEqual(days_remaining(2023, 6), 31)
        self.assertEqual(days_remaining(2023, 7), 30)
        self.assertEqual(days_remaining(2023, 8), 31)
        self.assertEqual(days_remaining(2023, 9), 30)
        self.assertEqual(days_remaining(2023, 10), 31)
        self.assertEqual(days_remaining(2023, 11), 30)
        self.assertEqual(days_remaining(2023, 12), 31)
    def test_non_leap_february(self):
        self.assertEqual(days_remaining(2023, 2), 2)
    def test_leap_year_february(self):
        self.assertEqual(days_remaining(2024, 2), 1)
    def test_leap_year_non_february(self):
        self.assertEqual(days_remaining(2024, 1), 30)
        self.assertEqual(days_remaining(2024, 3), 28)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)