from datetime import date, timedelta

def next_monday(timestamp):
    target_date = date.fromisoformat(timestamp)
    days_ahead = (6 - target_date.weekday()) % 7 + 1
    return target_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    sample_timestamp = '2024-02-28'
    print(next_monday(sample_timestamp))