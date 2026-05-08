import unittest
def determine_weekday(year, month, day):
    import calendar
    day_of_week = calendar.weekday(year, month, day)
    return day_of_week
class TestDetermineWeekday(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(determine_weekday(2023, 10, 25), 3)
        self.assertEqual(determine_weekday(2023, 10, 31), 4)
    def test_start_of_month(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2024, 5, 1), 3)
    def test_end_of_month(self):
        self.assertEqual(determine_weekday(2023, 12, 31), 2)
        self.assertEqual(determine_weekday(2024, 2, 29), 1)
    def test_leap_year(self):
        self.assertEqual(determine_weekday(2024, 2, 29), 1)
        self.assertEqual(determine_weekday(2028, 2, 29), 1)
    def test_different_months(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2023, 12, 31), 2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)