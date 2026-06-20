from datetime import datetime

def seconds_left_in_month(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    next_month = dt.replace(day=28) + timedelta(days=4)
    return (next_month - dt.replace(day=1)).total_seconds()
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))