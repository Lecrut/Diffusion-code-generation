from datetime import datetime, timedelta

def get_next_month(start_date):
    year = start_date.year
    month = start_date.month
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    return datetime(next_year, next_month, 1)

if __name__ == '__main__':
    start_date = datetime(2023, 11, 15)
    print(get_next_month(start_date))