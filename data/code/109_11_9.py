from datetime import datetime

def time_remaining(year, month):
    end_of_month = datetime(year, month + 1, 1) - timedelta(days=1)
    now = datetime.now()
    remaining_time = end_of_month - now
    return remaining_time.days * 24 + remaining_time.seconds // 3600, (remaining_time.seconds % 3600) // 60, remaining_time.seconds % 60

if __name__ == '__main__':
    print(time_remaining(2023, 10))