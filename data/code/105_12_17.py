from datetime import datetime, timedelta

def next_weekday(start_date, weekday):
    days_ahead = (weekday - start_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)
if __name__ == '__main__':
    reference_date = datetime(2023, 10, 1)
    target_weekday = 4
    next_friday = next_weekday(reference_date, target_weekday)
    print(next_friday.strftime('%Y-%m-%d'))