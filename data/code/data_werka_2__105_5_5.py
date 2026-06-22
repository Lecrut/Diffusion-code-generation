from datetime import date, timedelta

def next_wednesday_after(start_date: date) -> date:
    days_ahead = 2 - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    start = date(2023, 10, 10)
    result = next_wednesday_after(start)
    print(result)