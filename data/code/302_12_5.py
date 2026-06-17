class DateCalculator:
    def calculate_day_number(self, year, month):
        if not isinstance(year, int) or not isinstance(month, int):
            raise TypeError("Year and month must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= year <= 9999):
            raise ValueError("Year must be a valid four-digit number")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
        cumulative_days = 0
        for m in range(1, month):
            days = days_in_month[m]
            cumulative_days += days
        day_number = cumulative_days + month
        return day_number
if __name__ == '__main__':
    calculator = DateCalculator()
    year1, month1 = 2023, 1
    result1 = calculator.calculate_day_number(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Day Number: {result1}")
    year2, month2 = 2023, 2
    result2 = calculator.calculate_day_number(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Day Number: {result2}")
    year3, month3 = 2024, 2
    result3 = calculator.calculate_day_number(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Day Number: {result3}")
    year4, month4 = 2022, 12
    result4 = calculator.calculate_day_number(year4, month4)
    print(f"Year: {year4}, Month: {month4}, Day Number: {result4}")
    year5, month5 = 2000, 1
    result5 = calculator.calculate_day_number(year5, month5)
    print(f"Year: {year5}, Month: {month5}, Day Number: {result5}")
    try:
        calculator.calculate_day_number(2023, 13)
    except ValueError as e:
        print(f"Error caught for invalid month: {e}")
    try:
        calculator.calculate_day_number(99999, 1)
    except ValueError as e:
        print(f"Error caught for invalid year: {e}")