from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, '%B %d, %Y')
    days_ahead = (target_date.weekday() - 0) % 7
    return target_date + timedelta(days=7 - days_ahead)
if __name__ == '__main__':
    sample_timestamp = 'February 28, 2024'
    next_monday_date = next_monday(sample_timestamp)
    print(next_monday_date.strftime('%B %d, %Y'))