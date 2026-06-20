import unittest

def day_of_year(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        raise ValueError("Invalid date")
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    
    return sum(days_in_month[:month]) + day

class TestDayOfYear(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(day_of_year(2023, 1, 1), 1)
        self.assertEqual(day_of_year(2023, 12, 31), 365)
    
    def test_leap_year_feb_29(self):
        self.assertEqual(day_of_year(2024, 2, 29), 60)
    
    def test_non_leap_year_feb_28(self):
        self.assertEqual(day_of_year(2023, 2, 28), 59)

if __name__ == '__main__':
    print(day_of_year(2023, 1, 1))
    print(day_of_year(2023, 12, 31))
    print(day_of_year(2024, 2, 29))
    print(day_of_year(2023, 2, 28))

    unittest.main()