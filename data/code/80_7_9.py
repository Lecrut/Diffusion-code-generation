import unittest
from datetime import date

def compare_dates(date1: date, date2: date) -> str:
    if date1 == date2:
        return "Dates are identical"
    elif date1 < date2:
        return f"{date1} is earlier than {date2}"
    else:
        return f"{date1} is later than {date2}"

class TestDateComparison(unittest.TestCase):
    def test_identical_dates(self):
        self.assertEqual(compare_dates(date(2023, 4, 1), date(2023, 4, 1)), "Dates are identical")

    def test_earlier_date(self):
        self.assertEqual(compare_dates(date(2022, 12, 25), date(2023, 1, 1)), "2022-12-25 is earlier than 2023-01-01")

    def test_later_date(self):
        self.assertEqual(compare_dates(date(2024, 1, 1), date(2023, 12, 31)), "2024-01-01 is later than 2023-12-31")

    def test_different_months(self):
        self.assertEqual(compare_dates(date(2023, 5, 1), date(2023, 6, 1)), "2023-05-01 is earlier than 2023-06-01")

    def test_different_years(self):
        self.assertEqual(compare_dates(date(2022, 12, 31), date(2023, 1, 1)), "2022-12-31 is earlier than 2023-01-01")

if __name__ == '__main__':
    unittest.main()