import datetime
def calculate_remaining_days(year, month):
    current_date = datetime.date(year, month, 1)
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    last_day_of_next_month = (datetime.date(next_year, next_month, 1) + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    if next_month == 12:
        last_day_of_next_month = datetime.date(next_year, 12, 31)
    else:
        last_day_of_next_month = datetime.date(next_year, next_month, 1) + datetime.timedelta(days=31) - datetime.timedelta(days=1)
    days_difference = (last_day_of_next_month - current_date).days
    return days_difference
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    result = calculate_remaining_days(sample_year, sample_month)
    print(result)