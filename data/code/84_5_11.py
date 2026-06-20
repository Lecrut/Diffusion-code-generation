def get_day_number(year: int, month: int, day: int) -> int:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    sample_day = 15
    print(get_day_number(sample_year, sample_month, sample_day))