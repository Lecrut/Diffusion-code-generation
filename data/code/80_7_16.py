import unittest
from datetime import date

def compare_dates(date1: date, date2: date) -> str:
    if date1 == date2:
        return "Dates are identical"
    elif date1 < date2:
        return f"{date1} is before {date2}"
    else:
        return f"{date1} is after {date2}"

class TestDateComparison(unittest.TestCase):
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def format_date(date_obj: date) -> str:
        return date_obj.strftime(TestDateComparison.DATE_FORMAT)

    def test_identical_dates(self):
        self.assertEqual(compare_dates(date(2023, 4, 1), date(2023, 4, 1)), "Dates are identical")

    def test_date_before_another(self):
        result = compare_dates(date(2023, 3, 15), date(2023, 4, 1))
        self.assertEqual(result, f"{self.format_date(date(2023, 3, 15))} is before {self.format_date(date(2023, 4, 1))}")

    def test_date_after_another(self):
        result = compare_dates(date(2023, 5, 1), date(2023, 4, 1))
        self.assertEqual(result, f"{self.format_date(date(2023, 5, 1))} is after {self.format_date(date(2023, 4, 1))}")

    def test_different_years(self):
        result = compare_dates(date(2022, 12, 31), date(2023, 1, 1))
        self.assertEqual(result, f"{self.format_date(date(2022, 12, 31))} is before {self.format_date(date(2023, 1, 1))}")

if __name__ == '__main__':
    unittest.main()