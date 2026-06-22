from datetime import date
from typing import Union

def _validate_date_input(obj: Union[date, object]) -> date:
    if not isinstance(obj, date):
        raise ValueError("Expected a datetime.date instance")
    return obj

def get_days_delta(first: date, second: date) -> int:
    validated_first = _validate_date_input(first)
    validated_second = _validate_date_input(second)
    difference = validated_second - validated_first
    return difference.days

if __name__ == '__main__':
    start = date(2022, 11, 15)
    end = date(2023, 3, 10)
    delta_value = get_days_delta(start, end)
    print(delta_value)