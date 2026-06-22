from datetime import date, timedelta

MONDAY = 0

def find_next_monday(target_date: date) -> date:
    if not isinstance(target_date, date):
        raise ValueError("Argument must be a date instance")
    days_until_monday = (MONDAY - target_date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return target_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    reference_date = date(2024, 2, 28)
    next_monday = find_next_monday(reference_date)
    print(next_monday)