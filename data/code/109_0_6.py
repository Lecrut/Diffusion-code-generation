import datetime
def calculate_days_remaining(year, month, day):
    today = datetime.date.today()
    if month == today.month and year == today.year:
        days_remaining = (datetime.date(year, month + 1, 1) - today).days
    else:
        days_remaining = 0
    return days_remaining
if __name__ == '__main__':
    sample_year = 2024
    sample_month = 12
    sample_day = 31
    result = calculate_days_remaining(sample_year, sample_month, sample_day)
    print(result)