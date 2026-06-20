import unittest
from datetime import datetime

def get_next_month_first_day(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        return datetime(next_year, next_month, 1).strftime('%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e

class TestGetNextMonthFirstDay(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(get_next_month_first_day("2023-10-15"), "2023-11-01")
        self.assertEqual(get_next_month_first_day("2023-01-31"), "2023-02-01")

    def test_edge_cases(self):
        self.assertEqual(get_next_month_first_day("2023-12-31"), "2024-01-01")
        self.assertEqual(get_next_month_first_day("2020-02-29"), "2020-03-01")

    def test_invalid_dates(self):
        with self.assertRaises(ValueError) as context:
            get_next_month_first_day("2023/10/15")
        self.assertIn("Invalid date format", str(context.exception))

if __name__ == '__main__':
    unittest.main()