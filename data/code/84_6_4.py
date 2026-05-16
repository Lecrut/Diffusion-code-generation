import math
def get_day_number(year: int, month: int, day: int) -> int:
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            if day == 29:
                return 60 if month == 2 else 60                                                                                             
            else:
                return 31 + day
        else:
            return 31 + day
    else:
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days_in_feb = 29
            else:
                days_in_feb = 28
            return sum(days_in_month[:month]) + day
        else:
            return sum(days_in_month[:month]) + day
if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))
    print(get_day_number(2023, 2, 1))
    print(get_day_number(2023, 2, 28))
    print(get_day_number(2023, 2, 29))
    print(get_day_number(2023, 2, 30))
    print(get_day_number(2023, 2, 31))
    print(get_day_number(2024, 2, 1))
    print(get_day_number(2025, 12, 31))
    print(get_day_number(2000, 3, 1))
    print(get_day_number(1900, 3, 1))