from datetime import date, timedelta

def next_weekday(start_date, target_weekday):
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead < 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    start = date(2023, 10, 1)
    result = next_weekday(start, 4)
    print(result)