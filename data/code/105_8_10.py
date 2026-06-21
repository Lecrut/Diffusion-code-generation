from datetime import date, timedelta

def next_day_of_week(target_weekday, start_date):
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_date = start_date + timedelta(days=days_ahead)
    return next_date

if __name__ == '__main__':
    start = date(2023, 9, 15)
    target = 3
    result = next_day_of_week(target, start)
    print(result)