from datetime import date, timedelta

def compute_upcoming_saturday(reference: date) -> date:
    current_weekday_index = reference.weekday()
    target_weekday_index = 5
    days_offset = (target_weekday_index - current_weekday_index) % 7
    if days_offset == 0:
        days_offset = 7
    return reference + timedelta(days=days_offset)

if __name__ == '__main__':
    input_date = date(2023, 11, 1)
    next_saturday = compute_upcoming_saturday(input_date)
    print(next_saturday)