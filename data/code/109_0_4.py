import datetime
def calculate_days_remaining(year, month, day):
    today = datetime.date.today()
    if month == today.month and year == today.year:
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        return days_in_month - (day - 1)
    else:
        return -1
if __name__ == '__main__':
    target_year = 2024
    target_month = 12
    target_day = 25
    days_left = calculate_days_remaining(target_year, target_month, target_day)
    print(days_left)