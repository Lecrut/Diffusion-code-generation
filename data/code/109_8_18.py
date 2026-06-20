import datetime

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def days_left_in_month(year, month):
    today = datetime.date(year, month, 1)
    first_day_of_next_month = today.replace(day=28) + datetime.timedelta(days=4)
    if month == 12:
        next_month = today.replace(year=year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=month + 1, day=1)
    days_in_current_month = (next_month - today).days
    weekdays_left = [day for day in WEEKDAYS if day not in [today.strftime("%A")]]
    return days_in_current_month - len(weekdays_left)

if __name__ == '__main__':
    year = 2023
    month = 10
    days_left = days_left_in_month(year, month)
    print(days_left)