from datetime import date, timedelta

def get_upcoming_friday(reference_date: date) -> date:
    weekday = reference_date.weekday()
    days_until_friday = (4 - weekday) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    return reference_date + timedelta(days=days_until_friday)

if __name__ == '__main__':
    ref = date(2023, 12, 15)
    next_fri = get_upcoming_friday(ref)
    print(next_fri.strftime("%Y-%m-%d"))