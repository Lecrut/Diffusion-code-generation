from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, '%B %d, %Y')
    days_ahead = (target_date.weekday() - 0) % 7
    next_monday = target_date + timedelta(days=days_ahead + 7)
    return next_monday.strftime('%B %d, %Y')
if __name__ == '__main__':
    sample_timestamp = 'February 28, 2024'
    print(next_monday(sample_timestamp))