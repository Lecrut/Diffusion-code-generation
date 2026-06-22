def days_in_month(year, month):
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[2] = 29
    return month_days.get(month, 0)
if __name__ == '__main__':
    print(days_in_month(2023, 1))
    print(days_in_month(2023, 2))
    print(days_in_month(2024, 2))
    print(days_in_month(2023, 3))