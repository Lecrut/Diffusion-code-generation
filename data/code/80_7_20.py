import unittest
from datetime import date

class DateComparison:
    IDENTICAL_DATES_MSG = "Dates are identical"
    BEFORE_DATE_MSG = "{date1} is before {date2}"
    AFTER_DATE_MSG = "{date1} is after {date2}"

    @staticmethod
    def compare_dates(date1: date, date2: date) -> str:
        if not isinstance(date1, date) or not isinstance(date2, date):
            raise ValueError("Both inputs must be instances of the date class")
        if date1 == date2:
            return DateComparison.IDENTICAL_DATES_MSG
        elif date1 < date2:
            return DateComparison.BEFORE_DATE_MSG.format(date1=date1, date2=date2)
        else:
            return DateComparison.AFTER_DATE_MSG.format(date1=date1, date2=date2)

class TestDateComparison(unittest.TestCase):
    def test_identical_dates(self):
        self.assertEqual(DateComparison.compare_dates(date(2023, 4, 1), date(2023, 4, 1)), DateComparison.IDENTICAL_DATES_MSG)
    
    def test_date_before_another(self):
        self.assertEqual(DateComparison.compare_dates(date(2022, 12, 25), date(2023, 1, 1)), DateComparison.BEFORE_DATE_MSG.format(date1=date(2022, 12, 25), date2=date(2023, 1, 1)))
    
    def test_date_after_another(self):
        self.assertEqual(DateComparison.compare_dates(date(2024, 1, 1), date(2023, 12, 31)), DateComparison.AFTER_DATE_MSG.format(date1=date(2024, 1, 1), date2=date(2023, 12, 31)))

if __name__ == "__main__":
    unittest.main()