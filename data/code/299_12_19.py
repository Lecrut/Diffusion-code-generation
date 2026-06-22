import datetime

WEEKEND_DAYS = {5, 6}

def is_weekend(date_input):
    try:
        date = datetime.datetime.strptime(str(date_input), '%Y-%m-%d').date()
        return date.weekday() in WEEKEND_DAYS
    except ValueError:
        return False

if __name__ == '__main__':
    dates = ["2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-05"]
    for date in dates:
        print(f"{date} is weekend: {is_weekend(date)}")