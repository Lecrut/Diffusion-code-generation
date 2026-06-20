import unittest
from datetime import datetime, timedelta

class DateUtils:
    MONTHS_IN_YEAR = 12
    
    @staticmethod
    def get_next_month_first_day(date_string):
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        if month == DateUtils.MONTHS_IN_YEAR:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        next_date = datetime(next_year, next_month, 1)
        return next_date.strftime('%Y-%m-%d')

class TestDateUtils(unittest.TestCase):
    def test_next_month_first_day(self):
        self.assertEqual(DateUtils.get_next_month_first_day('2023-10-15'), '2023-11-01')
        self.assertEqual(DateUtils.get_next_month_first_day('2023-12-31'), '2024-01-01')

if __name__ == '__main__':
    unittest.main()