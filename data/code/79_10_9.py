from datetime import datetime, timedelta

def get_next_month_date(date):
    year = date.year
    month = date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return datetime(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(get_next_month_date(sample_date))