def days_in_month(year: int, month: int) -> int:
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12')
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_feb = 29
    else:
        days_in_feb = 28
    month_days = {1: 31, 2: days_in_feb, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return month_days[month]
if __name__ == '__main__':
    print(days_in_month(2023, 4))
    print(days_in_month(2024, 2))