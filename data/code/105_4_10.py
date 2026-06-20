import datetime

def nearest_saturday(date_obj):
    days_until_saturday = (5 - date_obj.weekday()) % 7
    if days_until_saturday == 0:
        days_until_saturday = 7
    return date_obj + datetime.timedelta(days=days_until_saturday)

if __name__ == '__main__':
    target_date = datetime.date(2023, 11, 1)
    upcoming_saturday = nearest_saturday(target_date)
    print(f"Nearest Upcoming Saturday: {upcoming_saturday}")