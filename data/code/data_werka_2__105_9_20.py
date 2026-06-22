from datetime import date, timedelta

def compute_next_monday(reference: date) -> date:
    if not isinstance(reference, date):
        raise TypeError("Expected a date object")
    current_weekday = reference.weekday()
    days_to_add = (7 - current_weekday) % 7
    if days_to_add == 0:
        days_to_add = 7
    return reference + timedelta(days=days_to_add)

if __name__ == '__main__':
    target = date(2024, 2, 28)
    next_monday = compute_next_monday(target)
    print(next_monday)