from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def timestamp_to_date(timestamp):
    date = datetime.fromtimestamp(timestamp)
    year, month, day = date.year, date.month, date.day
    if is_leap_year(year) and month > 2:
        day += 1
    return f'{year:04d}/{month:02d}/{day:02d}'

if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_date(sample_timestamp))