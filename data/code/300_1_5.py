import calendar
def days_remaining(target_month, year):
    if target_month == 12:
        days_in_month = 31
    else:
        days_in_month = calendar.monthrange(year, target_month)[1]
    return days_in_month
if __name__ == '__main__':
    print(days_remaining(1, 2023))
    print(days_remaining(12, 2023))
    print(days_remaining(2, 2024))
    print(days_remaining(9, 2023))