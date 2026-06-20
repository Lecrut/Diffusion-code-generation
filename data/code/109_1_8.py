from datetime import datetime

def seconds_left_in_month(timestamp):
    now = datetime.fromtimestamp(timestamp)
    next_month = now.replace(day=28) + timedelta(days=4)
    last_day_of_next_month = next_month - timedelta(days=next_month.day)
    return (last_day_of_next_month - now).total_seconds()
if __name__ == '__main__':
    timestamp = 1672531200
    print(seconds_left_in_month(timestamp))