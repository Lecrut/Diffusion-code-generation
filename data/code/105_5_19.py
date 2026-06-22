from datetime import date, timedelta
from typing import Optional

WEDNESDAY_INDEX = 2
WEEK_LENGTH = 7
MINIMUM_START_DATE = date(1, 1, 1)

def validate_date_input(d: date) -> date:
    if not isinstance(d, date):
        raise TypeError("Input must be a date instance")
    if d < MINIMUM_START_DATE:
        raise ValueError("Date cannot be before year 1")
    return d

def calculate_next_wednesday(start_date: date) -> date:
    validated_date = validate_date_input(start_date)
    current_weekday = validated_date.weekday()
    days_until_wednesday = (WEDNESDAY_INDEX - current_weekday + WEEK_LENGTH) % WEEK_LENGTH
    if days_until_wednesday == 0:
        days_until_wednesday = WEEK_LENGTH
    return validated_date + timedelta(days=days_until_wednesday)

if __name__ == '__main__':
    start_date = date(2023, 10, 10)
    result = calculate_next_wednesday(start_date)
    print(result)