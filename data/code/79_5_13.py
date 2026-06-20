import unittest
from datetime import datetime

class DateUtils:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def get_next_month_first_day(date_string):
        date_obj = datetime.strptime(date_string, cls.DATE_FORMAT)
        year = date_obj.year
        month = date_obj.month
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        next_date = datetime(next_year, next_month, 1)
        return next_date.strftime(cls.DATE_FORMAT)

class TestDateUtils(unittest.TestCase):
    def test_next_month_first_day(self):
        self.assertEqual(DateUtils.get_next_month_first_day("2023-10-15"), "2023-11-01")
        self.assertEqual(DateUtils.get_next_month_first_day("2023-12-31"), "2024-01-01")

if __name__ == '__main__':
    unittest.main()