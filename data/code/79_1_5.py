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
        return date(next_year, next_month, 1)
    except ValueError:
        return date(next_year, next_month, 1)
if __name__ == '__main__':
    sample_date = date(2023, 2, 28)
    print(get_next_month_date(sample_date))
    sample_date = date(2023, 12, 31)
    print(get_next_month_date(sample_date))