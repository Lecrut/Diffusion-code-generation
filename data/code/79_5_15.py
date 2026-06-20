import unittest
from datetime import datetime

def get_next_month_first_day(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    year, month = date_obj.year, date_obj.month
    if month == 12:
        return (year + 1, 1)
    else:
        return (year, month + 1)

class TestNextMonthFirstDay(unittest.TestCase):
    def test_regular_month(self):
        self.assertEqual(get_next_month_first_day("2023-10-15"), (2023, 11))

    def test_end_of_year(self):
        self.assertEqual(get_next_month_first_day("2023-12-31"), (2024, 1))

if __name__ == '__main__':
    unittest.main()