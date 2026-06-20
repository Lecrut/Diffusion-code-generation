import datetime
DAYS_IN_MONTH = 30

def calculate_days_remaining(year, month):
    today = datetime.date.today()
    if year == today.year and month == today.month:
        return DAYS_IN_MONTH - (today.day - 1)
    else:
        return 0
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    days_left = calculate_days_remaining(sample_year, sample_month)
    print(days_left)