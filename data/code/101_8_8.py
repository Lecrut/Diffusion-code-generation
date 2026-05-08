import unittest
def determine_weekday(year, month, day):
    import calendar
    return calendar.weekday(year, month, day)
class TestDetermineWeekday(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(determine_weekday(2023, 10, 26), 3)
        self.assertEqual(determine_weekday(2023, 10, 31), 2)
    def test_start_of_month(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2024, 5, 1), 3)
    def test_end_of_month(self):
        self.assertEqual(determine_weekday(2023, 12, 31), 2)
        self.assertEqual(determine_weekday(2024, 1, 31), 6)
    def test_leap_year(self):
        self.assertEqual(determine_weekday(2024, 2, 29), 3)
    def test_different_months(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2023, 12, 31), 2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)