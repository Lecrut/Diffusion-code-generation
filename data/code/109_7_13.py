from datetime import datetime, timedelta

def seconds_remaining_in_month():
    now = datetime.now()
    last_day_of_month = now.replace(day=28) + timedelta(days=4)
    last_day_of_month -= timedelta(days=last_day_of_month.day)
    return (last_day_of_month - now).total_seconds()

if __name__ == '__main__':
    print(seconds_remaining_in_month())