import unittest
def determine_weekday(year, month, day):
    import calendar
    try:
        weekday_num = calendar.weekday(year, month, day)
        return weekday_num
    except ValueError:
        return None
class TestDetermineWeekday(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(determine_weekday(2023, 10, 26), 3)
        self.assertEqual(determine_weekday(2023, 10, 27), 4)
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
    def test_month_start_edge_case(self):
        self.assertEqual(determine_weekday(2023, 1, 1), 0)
        self.assertEqual(determine_weekday(2024, 3, 1), 0)
    def test_month_end_edge_case(self):
        self.assertEqual(determine_weekday(2023, 1, 31), 2)
        self.assertEqual(determine_weekday(2023, 4, 30), 1)
        self.assertEqual(determine_weekday(2023, 2, 28), 1)
    def test_leap_year_edge_case(self):
        self.assertEqual(determine_weekday(2024, 2, 29), 3)
    def test_invalid_date(self):
        self.assertIsNone(determine_weekday(2023, 2, 30))
        self.assertIsNone(determine_weekday(2023, 13, 1))
        self.assertIsNone(determine_weekday(2023, 1, 130))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-action', 'excite'], exit=False)