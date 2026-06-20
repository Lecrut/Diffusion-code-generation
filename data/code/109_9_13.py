import datetime

def days_remaining_in_month():
    today = datetime.date.today()
    last_day_of_month = today.replace(day=28) + datetime.timedelta(days=4)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    remaining_days = days_remaining_in_month()
    print(remaining_days)