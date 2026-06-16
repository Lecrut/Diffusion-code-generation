class DateManager:
    def __init__(self):
        pass
    def get_day_of_month(self, year, month):
        if not (isinstance(year, int) and isinstance(month, int)):
            raise TypeError("Year and month must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            max_days = 29 if is_leap else 28
        else:
            max_days = days_in_month[month]
        return max_days
if __name__ == '__main__':
    manager = DateManager()
    year1 = 2024
    month1 = 2
    day1 = manager.get_day_of_month(year1, month1)
    print(f"Day of the month for {year1}-{month1}: {day1}")
    year2 = 2023
    month2 = 12
    day2 = manager.get_day_of_month(year2, month2)
    print(f"Day of the month for {year2}-{month2}: {day2}")
    year3 = 2024
    month3 = 4
    day3 = manager.get_day_of_month(year3, month3)
    print(f"Day of the month for {year3}-{month3}: {day3}")