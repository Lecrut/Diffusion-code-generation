import datetime
def calculate_days_remaining(year, month, day):
    today = datetime.date.today()
    if month == today.month and year == today.year:
        if day > today.day:
            return day - today.day
        else:
            return 0
    else:
        target_date = datetime.date(year, month, day)
        if target_date > today:
            delta = target_date - today
            return delta.days
        else:
            return -abs(target_date - today).days
if __name__ == '__main__':
    sample_year = 2024
    sample_month = 12
    sample_day = 31
    days_left = calculate_days_remaining(sample_year, sample_month, sample_day)
    print(days_left)