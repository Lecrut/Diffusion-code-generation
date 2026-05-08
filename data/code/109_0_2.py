import datetime
def calculate_days_remaining(year, month, day):
    today = datetime.date.today()
    if month == today.month and year == today.year:
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        if day > days_in_month:
            return -days_in_month
        else:
            return days_in_month - (day - 1)
    else:
        return 0
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 12
    sample_day = 25
    result = calculate_days_remaining(sample_year, sample_month, sample_day)
    print(result)