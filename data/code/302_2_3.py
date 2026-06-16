class DateManager:
    def __init__(self):
        pass
    def get_day_of_month(self, year, month):
        if not (isinstance(year, int) and isinstance(month, int)):
            raise TypeError("Year and month must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if is_leap:
                return 29
            else:
                return 28
        else:
            return days_in_month[month - 1]
if __name__ == '__main__':
    manager = DateManager()
    year1 = 2023
    month1 = 10
    day1 = manager.get_day_of_month(year1, month1)
    print(f"The number of days in {month1}/{year1} is: {day1}")
    year2 = 2024
    month2 = 2
    day2 = manager.get_day_of_month(year2, month2)
    print(f"The number of days in {month2}/{year2} is: {day2}")
    year3 = 2023
    month3 = 1
    day3 = manager.get_day_of_month(year3, month3)
    print(f"The number of days in {month3}/{year3} is: {day3}")