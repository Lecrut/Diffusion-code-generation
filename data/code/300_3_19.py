from datetime import date

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)

if __name__ == '__main__':
    today = date.today()
    last_day = last_day_of_month(today)
    days_left = (last_day - today).days
    print(days_left)