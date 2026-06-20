from datetime import datetime, timedelta

def seconds_left_in_month(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    _, month, year = (dt.year, dt.month, dt.day)
    if month == 12:
        next_year = year + 1
        last_day_of_this_month = datetime(next_year, month, 31)
    else:
        next_year = year
        last_day_of_this_month = datetime(year, month + 1, 1) - timedelta(days=1)
    return (last_day_of_this_month - dt).total_seconds()
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))