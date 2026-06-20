import datetime

def get_remaining_minutes():
    current_date = datetime.datetime.now()
    last_day_of_month = current_date.replace(day=current_date.month + 1, hour=0, minute=0, second=0) - datetime.timedelta(days=1)
    remaining_time = last_day_of_month - current_date
    return remaining_time.total_seconds() / 60

if __name__ == '__main__':
    print(get_remaining_minutes())