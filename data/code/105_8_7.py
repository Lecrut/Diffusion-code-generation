from datetime import datetime, timedelta

def next_weekday(date, weekday):
    days_ahead = (weekday - date.weekday() + 7) % 7
    return date + timedelta(days=days_ahead)
if __name__ == '__main__':
    target_date = datetime(2023, 9, 15)
    day_of_week = 3
    next_thursday = next_weekday(target_date, day_of_week)
    print(next_thursday.strftime('%Y-%m-%d'))