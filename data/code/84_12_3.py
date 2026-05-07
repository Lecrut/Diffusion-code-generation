class DateCalculator:
    def get_day_of_year(self, year, month, day):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
        day_of_year = 0
        for m in range(1, month):
            day_of_year += days_in_month[m]
        day_of_year += day
        return day_of_year
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = 26
    result1 = calculator.get_day_of_year(year1, month1, day1)
    print(f"Day of the year for {year1}-{month1:02d}-{day1:02d}: {result1}")
    year2 = 2000
    month2 = 3
    day2 = 1
    result2 = calculator.get_day_of_year(year2, month2, day2)
    print(f"Day of the year for {year2}-{month2:02d}-{day2:02d}: {result2}")
    year3 = 2024
    month3 = 2
    day3 = 29
    result3 = calculator.get_day_of_year(year3, month3, day3)
    print(f"Day of the year for {year3}-{month3:02d}-{day3:02d}: {result3}")
    year4 = 2023
    month4 = 1
    day4 = 1
    result4 = calculator.get_day_of_year(year4, month4, day4)
    print(f"Day of the year for {year4}-{month4:02d}-{day4:02d}: {result4}")