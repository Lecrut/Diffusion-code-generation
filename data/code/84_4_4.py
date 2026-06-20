import unittest

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be at least 1")
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    return sum(days_in_month[:month-1]) + day

class TestDayOfYear(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(day_of_year(2023, 1, 1), 1)
        self.assertEqual(day_of_year(2023, 12, 31), 365)

    def test_february_29th_leap_year(self):
        self.assertEqual(day_of_year(2024, 2, 29), 60)

    def test_february_28th_non_leap_year(self):
        self.assertEqual(day_of_year(2023, 2, 28), 59)

if __name__ == '__main__':
    print(day_of_year(2023, 1, 1))
    print(day_of_year(2023, 12, 31))
    print(day_of_year(2024, 2, 29))
    print(day_of_year(2023, 2, 28))

    unittest.main()