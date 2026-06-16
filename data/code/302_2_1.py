class DateCalculator:
    def get_day_of_month(self, year, month):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            max_days = 29 if is_leap else 28
        else:
            max_days = days_in_month[month]
        if not (1 <= year <= 9999):
             raise ValueError("Year must be a valid year")
        return max_days
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = calculator.get_day_of_month(year1, month1)
    print(f"The number of days in month {month1} of year {year1} is: {day1}")
    year2 = 2024
    month2 = 2
    day2 = calculator.get_day_of_month(year2, month2)
    print(f"The number of days in month {month2} of year {year2} is: {day2}")
    year3 = 2023
    month3 = 1
    day3 = calculator.get_day_of_month(year3, month3)
    print(f"The number of days in month {month3} of year {year3} is: {day3}")