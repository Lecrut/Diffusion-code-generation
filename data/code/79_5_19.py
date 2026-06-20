import unittest
from datetime import date

NEXT_MONTH = 1
NEXT_YEAR = 1

def get_next_month_first_day(date_string):
    current_date = date.fromisoformat(date_string)
    year = current_date.year
    month = current_date.month
    
    if month == 12:
        next_year += YEAR
        next_month = NEXT_MONTH
    else:
        next_month += NEXT_MONTH
        next_year = year
    
    next_date = date(next_year, next_month, 1)
    return next_date.isoformat()

class TestNextMonthFirstDay(unittest.TestCase):
    def test_middle_of_the_year(self):
        self.assertEqual(get_next_month_first_day("2023-10-15"), "2023-11-01")
    
    def test_end_of_the_year(self):
        self.assertEqual(get_next_month_first_day("2023-12-31"), "2024-01-01")
    
    def test_new_year(self):
        self.assertEqual(get_next_month_first_day("2023-01-01"), "2023-02-01")

if __name__ == '__main__':
    unittest.main()