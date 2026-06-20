from datetime import datetime, timedelta

def next_15th_day_of_month(date):
    year = date.year
    month = date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return datetime(year, month, 15)

if __name__ == '__main__':
    sample_date = datetime(2023, 3, 3)
    next_date = next_15th_day_of_month(sample_date)
    print(next_date)