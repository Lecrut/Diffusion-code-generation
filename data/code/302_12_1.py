class DateCalculator:
    def calculate_day_number(self, year, month):
        if not isinstance(year, int) or not isinstance(month, int):
            raise TypeError("Year and month must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_in_month[2] = 29 if is_leap else 28
        day_number = 0
        for m in range(1, month):
            days_in_month[m] = sum(days_in_month[:m])
        day_number = days_in_month[month - 1]
        return day_number
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 5
    result1 = calculator.calculate_day_number(year1, month1)
    print(f"Day number for {year1}-{month1}: {result1}")
    year2 = 2023
    month2 = 2
    result2 = calculator.calculate_day_number(year2, month2)
    print(f"Day number for {year2}-{month2}: {result2}")
    year3 = 2024
    month3 = 2
    result3 = calculator.calculate_day_number(year3, month3)
    print(f"Day number for {year3}-{month3}: {result3}")
    year4 = 2023
    month4 = 1
    result4 = calculator.calculate_day_number(year4, month4)
    print(f"Day number for {year4}-{month4}: {result4}")
    year5 = 2023
    month5 = 4
    result5 = calculator.calculate_day_number(year5, month5)
    print(f"Day number for {year5}-{month5}: {result5}")
    year6 = 2023
    month6 = 3
    result6 = calculator.calculate_day_number(year6, month6)
    print(f"Day number for {year6}-{month6}: {result6}")