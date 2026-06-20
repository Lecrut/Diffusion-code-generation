from datetime import datetime, timedelta

def days_in_month(year, month):
    if month == 12:
        return 31
    next_month = datetime(year, month + 1, 1)
    first_day_of_next_month = next_month.replace(day=1)
    last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
    return last_day_of_current_month.day

def seconds_left_in_month(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    current_year, current_month = dt.year, dt.month
    if not (1 <= current_month <= 12):
        raise ValueError("Invalid month. Month should be between 1 and 12.")
    
    last_day_of_current_month = days_in_month(current_year, current_month)
    seconds_left = (datetime(current_year, current_month, last_day_of_current_month) - dt).total_seconds()
    return int(seconds_left)

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))