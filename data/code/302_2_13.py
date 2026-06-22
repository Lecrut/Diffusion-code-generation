def day_number_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12')
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    return days_in_month[month - 1]
if __name__ == '__main__':
    print(day_number_in_month(2023, 2))
    print(day_number_in_month(2024, 2))