from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = timestamp + timedelta(days=(7 - timestamp.weekday()) % 7)
    return target_date

if __name__ == '__main__':
    sample_timestamp = datetime(2024, 2, 28)
    print(next_monday(sample_timestamp))