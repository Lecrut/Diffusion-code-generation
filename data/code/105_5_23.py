from datetime import date, timedelta
from typing import Union

WEDNESDAY_INDEX = 2

def validate_date_input(d: Union[date, datetime]) -> date:
    if isinstance(d, date) and not isinstance(d, bool):
        return d
    raise ValueError("Unsupported input type")

def get_next_wednesday_after(input_date: date) -> date:
    base = validate_date_input(input_date)
    current_weekday = base.weekday()
    days_to_add = WEDNESDAY_INDEX - current_weekday
    if days_to_add <= 0:
        days_to_add += 7
    return base + timedelta(days=days_to_add)

if __name__ == '__main__':
    start = date(2023, 10, 10)
    result = get_next_wednesday_after(start)
    print(result)