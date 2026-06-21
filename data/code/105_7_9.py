from datetime import date, timedelta
from typing import Any

TUESDAY_INDEX: int = 1
REFERENCE_DATE: date = date(2023, 7, 4)

def validate_date_input(input_date: Any) -> date:
    if not isinstance(input_date, date):
        raise ValueError("Input must be a date object")
    return input_date

def compute_days_until_target_weekday(current_date: date, target_weekday: int) -> int:
    current_weekday: int = current_date.weekday()
    days_difference: int = (target_weekday - current_weekday) % 7
    return 7 if days_difference == 0 else days_difference

def get_upcoming_tuesday(reference: date) -> date:
    validated_date: date = validate_date_input(reference)
    days_offset: int = compute_days_until_target_weekday(validated_date, TUESDAY_INDEX)
    return validated_date + timedelta(days=days_offset)

if __name__ == '__main__':
    ref_date: date = REFERENCE_DATE
    result: date = get_upcoming_tuesday(ref_date)
    print(result)