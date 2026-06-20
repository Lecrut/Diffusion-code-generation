from datetime import datetime, timedelta

def time_remaining(year, month):
    today = datetime.now()
    target_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
    remaining_time = target_date - today
    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

if __name__ == '__main__':
    print(time_remaining(2024, 1))