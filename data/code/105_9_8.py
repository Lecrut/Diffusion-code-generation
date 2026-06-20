from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, '%Y-%m-%d')
    days_ahead = (target_date.weekday() - 0) % 7
    next_monday = target_date + timedelta(days=(7 - days_ahead))
    return next_monday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_timestamp = '2024-02-28'
    print(next_monday(sample_timestamp))