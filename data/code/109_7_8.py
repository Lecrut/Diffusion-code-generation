from datetime import datetime, timedelta

def seconds_remaining_in_month():
    now = datetime.now()
    end_of_month = datetime(now.year, now.month + 1, 1) - timedelta(days=1)
    return (end_of_month - now).total_seconds()

if __name__ == '__main__':
    print(seconds_remaining_in_month())