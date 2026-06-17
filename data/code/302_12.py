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
    month1 = 10
    result1 = calculator.calculate_day_number(year1, month1)
    print(f"Day number for {year1}-{month1}: {result1}")
    year2 = 2024
    month2 = 2
    result2 = calculator.calculate_day_number(year2, month2)
    print(f"Day number for {year2}-{month2}: {result2}")
    year3 = 2022
    month3 = 12
    result3 = calculator.calculate_day_number(year3, month3)
    print(f"Day number for {year3}-{month3}: {result3}")
    year4 = 2021
    month4 = 1
    result4 = calculator.calculate_day_number(year4, month4)
    print(f"Day number for {year4}-{month4}: {result4}")
    year5 = 2021
    month5 = 2
    result5 = calculator.calculate_day_number(year5, month5)
    print(f"Day number for {year5}-{month5}: {result5}")