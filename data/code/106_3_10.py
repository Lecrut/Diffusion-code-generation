class DateDifferenceCalculator:
    EPOCH_YEAR = 1970

    @staticmethod
    def calculate_age_difference(date_str1, date_str2):
        year1, month1, day1 = map(int, date_str1.split('-'))
        year2, month2, day2 = map(int, date_str2.split('-'))
        
        if year1 > year2:
            return DateDifferenceCalculator.calculate_age_difference(date_str2, date_str1)
        
        days_in_year = 365 + (year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0)
        days_passed = sum(365 if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else 365 for y in range(DateDifferenceCalculator.EPOCH_YEAR, year1))
        days_passed += sum((month > m) + (month == m and day > d) for m, d in ((1, 31), (2, 28 if year1 % 4 != 0 or (year1 % 100 == 0 and year1 % 400 != 0) else 29), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)))
        days_passed += sum((month > m) + (month == m and day > d) for m, d in ((1, 31), (2, 28 if year2 % 4 != 0 or (year2 % 100 == 0 and year2 % 400 != 0) else 29), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, day2)))
        
        age_diff = days_passed // days_in_year
        return age_diff

if __name__ == '__main__':
    date1 = "1990-05-15"
    date2 = "2023-04-10"
    print(DateDifferenceCalculator.calculate_age_difference(date1, date2))