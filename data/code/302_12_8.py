class DateCalculator:
    def calculate_day_number(self, year, month):
        if not isinstance(year, int) or not isinstance(month, int):
            raise TypeError("Year and month must be integers.")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= year <= 9999):
            raise ValueError("Year must be a valid calendar year.")
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
    year1 = 2023
    month1 = 1
    result1 = calculator.calculate_day_number(year1, month1)
    print(f"Day number for {year1}-{month1}: {result1}")
    year2 = 2023
    month2 = 3
    result2 = calculator.calculate_day_number(year2, month2)
    print(f"Day number for {year2}-{month2}: {result2}")
    year3 = 2024
    month3 = 2
    result3 = calculator.calculate_day_number(year3, month3)
    print(f"Day number for {year3}-{month3}: {result3}")
    year4 = 2025
    month4 = 12
    result4 = calculator.calculate_day_number(year4, month4)
    print(f"Day number for {year4}-{month4}: {result4}")
    year5 = 2028
    month5 = 2
    result5 = calculator.calculate_day_number(year5, month5)
    print(f"Day number for {year5}-{month5}: {result5}")