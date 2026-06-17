def day_number(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    return sum(days_in_month[:month]) + month
if __name__ == '__main__':
    print(day_number(2023, 1))
    print(day_number(2024, 2))
    print(day_number(2000, 3))
    print(day_number(2023, 2))