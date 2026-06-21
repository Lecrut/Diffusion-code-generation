from datetime import date, timedelta

WEDNESDAY_INDEX = 2
WEEK_LENGTH = 7

def validate_date_input(target: date) -> None:
    if not isinstance(target, date):
        raise ValueError("Input must be a date object")
    if target < date(1, 1, 1):
        raise ValueError("Date cannot be before year 1")

def calculate_days_until_target(current: date, target_weekday: int) -> int:
    current_weekday = current.weekday()
    difference = target_weekday - current_weekday
    if difference <= 0:
        return WEEK_LENGTH + difference
    return difference

def find_next_occurrence(start: date, target_weekday: int) -> date:
    validate_date_input(start)
    days_to_add = calculate_days_until_target(start, target_weekday)
    return start + timedelta(days=days_to_add)

if __name__ == '__main__':
    start_date = date(2023, 10, 10)
    next_wed = find_next_occurrence(start_date, WEDNESDAY_INDEX)
    print(next_wed)