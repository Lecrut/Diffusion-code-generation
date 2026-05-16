import unittest
from datetime import date
from dateutil.relativedelta import relativedelta
def get_next_month(target_date):
    next_month = target_date + relativedelta(months=1)
    return next_month.date()
class TestNextMonth(unittest.TestCase):
    def test_standard_month_transition(self):
        test_date = date(2023, 10, 15)
        expected_date = date(2023, 11, 15)
        self.assertEqual(get_next_month(test_date), expected_date)
    def test_year_boundary(self):
        test_date = date(2023, 12, 31)
        expected_date = date(2024, 1, 31)
        self.assertEqual(get_next_month(test_date), expected_date)
    def test_month_end_transition(self):
        test_date = date(2023, 1, 31)
        expected_date = date(2023, 2, 28)
        self.assertEqual(get_next_month(test_date), expected_date)
    def test_non_leap_year_february_end(self):
        test_date = date(2023, 2, 28)
        expected_date = date(2023, 3, 28)
        self.assertEqual(get_next_month(test_date), expected_date)
    def test_leap_year_february_end(self):
        test_date = date(2024, 2, 29)
        expected_date = date(2024, 3, 29)
        self.assertEqual(get_next_month(test_date), expected_date)
    def test_single_digit_month(self):
        test_date = date(2023, 9, 5)
        expected_date = date(2023, 10, 5)
        self.assertEqual(get_next_month(test_date), expected_date)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)