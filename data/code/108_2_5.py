class DateCalculator:
    def get_day_of_month(self, year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Invalid month: Month must be between 1 and 12.")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day: Day must be between 1 and 31.")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            max_days = 29 if is_leap else 28
            if day > max_days:
                raise ValueError(f"Invalid day for February in {year}: {day}")
            return day
        else:
            if day > days_in_month[month]:
                raise ValueError(f"Invalid day for month {month} in {year}: {day}")
            return day
if __name__ == '__main__':
    calculator = DateCalculator()
    try:
        result1 = calculator.get_day_of_month(2023, 10, 25)
        print(f"Date 2023-10-25: Day of month is {result1}")
    except ValueError as e:
        print(f"Error for 2023-10-25: {e}")
    try:
        result2 = calculator.get_day_of_month(2024, 2, 29)
        print(f"Date 2024-02-29: Day of month is {result2}")
    except ValueError as e:
        print(f"Error for 2024-02-29: {e}")
    try:
        result3 = calculator.get_day_of_month(2023, 2, 29)
        print(f"Date 2023-02-29: Day of month is {result3}")
    except ValueError as e:
        print(f"Error for 2023-02-29: {e}")
    try:
        result4 = calculator.get_day_of_month(2023, 13, 15)
        print(f"Date 2023-13-15: Day of month is {result4}")
    except ValueError as e:
        print(f"Error for 2023-13-15: {e}")
    try:
        result5 = calculator.get_day_of_month(2023, 4, 31)
        print(f"Date 2023-04-31: Day of month is {result5}")
    except ValueError as e:
        print(f"Error for 2023-04-31: {e}")
    try:
        result6 = calculator.get_day_of_month(2023, 2, 30)
        print(f"Date 2023-02-30: Day of month is {result6}")
    except ValueError as e:
        print(f"Error for 2023-02-30: {e}")