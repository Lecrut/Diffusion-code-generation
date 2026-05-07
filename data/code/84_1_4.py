import calendar
def calculate_day_of_year(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[2] = 29
    cumulative_days = 0
    for m in range(1, month):
        cumulative_days += days_in_month[m]
    cumulative_days += day
    return cumulative_days
if __name__ == '__main__':
    print(calculate_day_of_year(2023, 10, 26))
    print(calculate_day_of_year(2024, 1, 1))
    print(calculate_day_of_year(2000, 2, 29))
    print(calculate_day_of_year(2023, 12, 31))
    print(calculate_day_of_year(2023, 3, 1))
    print(calculate_day_of_year(2023, 1, 1))