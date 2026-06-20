from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, '%Y-%m-%d')
    days_ahead = (6 - target_date.weekday()) % 7 + 1
    return (target_date + timedelta(days=days_ahead)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_timestamp = '2024-02-28'
    print(next_monday(sample_timestamp))