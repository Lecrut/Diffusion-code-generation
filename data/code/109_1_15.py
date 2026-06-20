def seconds_left_in_month(timestamp):
    from datetime import datetime, timedelta

    dt = datetime.fromtimestamp(timestamp)
    year = dt.year
    month = dt.month

    if month == 12:
        first_day_of_next_month = datetime(year + 1, 1, 1)
    else:
        first_day_of_next_month = datetime(year, month + 1, 1)

    last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
    seconds_in_month = (last_day_of_current_month - dt).total_seconds()
    
    return int(seconds_in_month)

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))