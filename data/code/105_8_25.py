from datetime import date, timedelta

def next_weekday(target_weekday: int, start_date: date) -> date:
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_day = 3
    result = next_weekday(target_day, start_date)
    print(result)