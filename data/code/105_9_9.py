from datetime import date, timedelta
DAYS_IN_WEEK = 7

def next_monday(timestamp):
    target_date = date.fromisoformat(timestamp)
    days_ahead = (6 - target_date.weekday()) % DAYS_IN_WEEK + 1
    return (target_date + timedelta(days=days_ahead)).strftime('%Y-%m-%d')
if __name__ == '__main__':
    sample_timestamp = '2024-02-28'
    print(next_monday(sample_timestamp))