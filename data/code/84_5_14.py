def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_number(year: int, month: int, day: int) -> int:
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:month - 1]) + day
if __name__ == '__main__':
    print(get_day_number(2020, 2, 29))
    print(get_day_number(2021, 2, 28))