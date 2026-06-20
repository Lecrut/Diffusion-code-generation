from datetime import datetime

def remaining_minutes_in_month():
    today = datetime.now()
    last_day_of_month = today.replace(day=28) + timedelta(days=4)
    last_day_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)
    return (last_day_of_month - today).seconds // 60

if __name__ == '__main__':
    print(remaining_minutes_in_month())