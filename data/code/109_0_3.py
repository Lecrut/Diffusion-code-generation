import datetime
def calculate_days_remaining(year, month, day):
    today = datetime.date.today()
    if month == today.month and year == today.year:
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        return days_in_month - (day - 1)
    else:
        return -1
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    days_left = calculate_days_remaining(sample_year, sample_month, sample_day)
    print(days_left)