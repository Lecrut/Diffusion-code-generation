from datetime import date, timedelta

def get_next_month_date(input_date):
    year = input_date.year
    month = input_date.month
    day = input_date.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    try:
        next_month_first_day = date(year, month, 1)
    except ValueError:
        next_month_first_day = date(year + (month == 2), month, 1)
    return next_month_first_day
if __name__ == '__main__':
    sample_date = date(2023, 1, 15)
    print(get_next_month_date(sample_date))