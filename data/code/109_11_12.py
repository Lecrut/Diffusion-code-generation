from datetime import datetime

def time_remaining(year, month):
    now = datetime.now()
    target_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
    delta = target_date - now
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

if __name__ == '__main__':
    print(time_remaining(2024, 1))