import unittest

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]:
        raise ValueError("Day must be within the valid range for the given month")
    if month == 2 and day == 29:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            raise ValueError("February 29th is not a leap year")
    return sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]) + day

class TestDayOfYear(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(day_of_year(2023, 1, 1), 1)
        self.assertEqual(day_of_year(2023, 12, 31), 365)

    def test_february_29th_leap_year(self):
        self.assertEqual(day_of_year(2024, 2, 29), 60)

    def test_february_28th_non_leap_year(self):
        self.assertEqual(day_of_year(2023, 2, 28), 59)

if __name__ == '__main__':
    print(day_of_year(2024, 2, 29))
    unittest.main()