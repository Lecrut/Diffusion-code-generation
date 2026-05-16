import unittest
def determine_weekday(year, month, day):
    import calendar
    return calendar.weekday(year, month, day)
class TestDetermineWeekday(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(determine_weekday(2023, 10, 26), 3)
        self.assertEqual(determine_weekday(2023, 10, 27), 4)
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
    def test_month_start_edge_case(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2024, 3, 1), 0)
    def test_month_end_edge_case(self):
        self.assertEqual(determine_weekday(2023, 1, 31), 6)
        self.assertEqual(determine_weekday(2023, 4, 30), 5)
        self.assertEqual(determine_weekday(2023, 2, 28), 5)
        self.assertEqual(determine_weekday(2024, 2, 29), 6)
    def test_leap_year_dates(self):
        self.assertEqual(determine_weekday(2024, 2, 29), 6)
    def test_different_months(self):
        self.assertEqual(determine_weekday(2023, 12, 31), 6)
        self.assertEqual(determine_weekday(2023, 9, 30), 5)
        self.assertEqual(determine_weekday(2023, 2, 28), 5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)