from datetime import datetime, timedelta

def next_weekday(start_date, weekday):
    days_ahead = (weekday - start_date.weekday() + 7) % 7
    return start_date + timedelta(days=days_ahead)
if __name__ == '__main__':
    start_date = datetime(2023, 9, 15)
    target_weekday = 3
    next_thursday = next_weekday(start_date, target_weekday)
    print(next_thursday.strftime('%Y-%m-%d'))