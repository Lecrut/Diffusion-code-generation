from datetime import date, timedelta

def get_next_month_date(input_date):
    year = input_date.year
    month = input_date.month
    day = input_date.day
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    try:
        next_month_first_day = date(next_year, next_month, 1)
    except ValueError:
        next_month_first_day = date(next_year, next_month, 1)
    return next_month_first_day
if __name__ == '__main__':
    sample_date = date(2023, 2, 28)
    print(get_next_month_date(sample_date))