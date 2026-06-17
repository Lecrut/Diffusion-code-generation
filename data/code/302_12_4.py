class DateCalculator:
    def calculate_day_number(self, year, month):
        if not isinstance(year, int) or not isinstance(month, int):
            raise TypeError("Year and month must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1900 <= year <= 3000):
            raise ValueError("Year out of reasonable range")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
        cumulative_days = 0
        for m in range(1, month):
            days = days_in_month[m]
            cumulative_days += days
        day_number = cumulative_days + 1
        return day_number
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 1
    day1 = calculator.calculate_day_number(year1, month1)
    print(f"Day number for {year1}-{month1}: {day1}")
    year2 = 2024
    month2 = 3
    day2 = calculator.calculate_day_number(year2, month2)
    print(f"Day number for {year2}-{month2}: {day2}")
    year3 = 2000
    month3 = 2
    day3 = calculator.calculate_day_number(year3, month3)
    print(f"Day number for {year3}-{month3}: {day3}")
    year4 = 2022
    month4 = 12
    day4 = calculator.calculate_day_number(year4, month4)
    print(f"Day number for {year4}-{month4}: {day4}")
    year5 = 1999
    month5 = 1
    day5 = calculator.calculate_day_number(year5, month5)
    print(f"Day number for {year5}-{month5}: {day5}")