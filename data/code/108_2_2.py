class DateCalculator:
    def get_day_of_month(self, year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Invalid month: Month must be between 1 and 12.")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day: Day must be between 1 and 31.")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if is_leap:
                max_days = 29
            else:
                max_days = 28
            if day > max_days:
                raise ValueError(f"Invalid day for February in {year}: {day}")
            return day
        else:
            max_days = days_in_month[month]
            if day > max_days:
                raise ValueError(f"Invalid day for month {month} in {year}: {day}")
            return day
if __name__ == '__main__':
    calculator = DateCalculator()
    print(f"Day of month for 2023, 10, 25: {calculator.get_day_of_month(2023, 10, 25)}")
    print(f"Day of month for 2024, 2, 29 (Leap year): {calculator.get_day_of_month(2024, 2, 29)}")
    print(f"Day of month for 2023, 2, 28: {calculator.get_day_of_month(2023, 2, 28)}")
    print(f"Day of month for 2023, 4, 30: {calculator.get_day_of_month(2023, 4, 30)}")
    try:
        calculator.get_day_of_month(2023, 13, 15)
    except ValueError as e:
        print(f"Error caught for invalid month: {e}")
    try:
        calculator.get_day_of_month(2023, 2, 29)
    except ValueError as e:
        print(f"Error caught for invalid day (Feb 29 in non-leap year): {e}")
    try:
        calculator.get_day_of_month(2023, 4, 31)
    except ValueError as e:
        print(f"Error caught for invalid day (April 31): {e}")