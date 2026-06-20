from datetime import datetime

def seconds_left_in_month(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    last_day_of_month = dt.replace(day=28) + timedelta(days=4)
    return (last_day_of_month - dt).seconds
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))