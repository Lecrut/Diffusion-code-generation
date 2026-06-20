from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def timestamp_to_date(timestamp):
    if not isinstance(timestamp, int) or timestamp < 0:
        raise ValueError("Invalid timestamp")
    
    epoch = datetime(1970, 1, 1)
    delta = timedelta(seconds=timestamp)
    date = epoch + delta
    return date.strftime('%Y/%m/%d')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatted_date = timestamp_to_date(sample_timestamp)
    print(formatted_date)