from datetime import datetime

def time_remaining(year, month):
    end_of_month = datetime(year, month + 1, 1) - timedelta(days=1)
    now = datetime.now()
    remaining_time = end_of_month - now
    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

if __name__ == '__main__':
    print(time_remaining(2023, 10))