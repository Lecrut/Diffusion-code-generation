from datetime import datetime, timedelta

def seconds_left_in_month(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    next_month = dt.replace(day=28) + timedelta(days=4)
    last_day_of_next_month = next_month - timedelta(days=next_month.day)
    return (last_day_of_next_month - dt).total_seconds()
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))