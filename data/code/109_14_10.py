import datetime

def days_until_end_of_month(date):
    year, month = (date.year, date.month)
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    days_in_month = (next_month_start - date).days
    return days_in_month
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    print(f'Days left until the end of the month for {sample_date}: {days_until_end_of_month(sample_date)}')