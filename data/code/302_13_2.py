def day_number(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_feb = 29
    else:
        days_in_feb = 28
    cumulative_days = 0
    for m in range(1, month):
        days = days_in_month[m-1]
        if m == 2:
            days = days_in_feb
        cumulative_days += days
    return cumulative_days + month
if __name__ == '__main__':
    print(day_number(2024, 3))
    print(day_number(2023, 2))
    print(day_number(2000, 3))
    print(day_number(2100, 2))