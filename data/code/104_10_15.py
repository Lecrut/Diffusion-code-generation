from datetime import date
from typing import Tuple

def validate_date_inputs(first: date, second: date) -> Tuple[date, date]:
    if not isinstance(first, date):
        raise ValueError("first argument must be a date instance")
    if not isinstance(second, date):
        raise ValueError("second argument must be a date instance")
    return (first, second)

def compare_dates(first: date, second: date) -> int:
    validated_first, validated_second = validate_date_inputs(first, second)
    if validated_first > validated_second:
        return 1
    if validated_first < validated_second:
        return -1
    return 0

if __name__ == '__main__':
    date_a: date = date(2024, 1, 15)
    date_b: date = date(2024, 1, 10)
    comparison_result: int = compare_dates(date_a, date_b)
    print(comparison_result)