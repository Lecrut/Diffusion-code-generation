from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
EXPECTED_ARGUMENT_COUNT = 2

def days_between(date_str_one: str, date_str_two: str) -> int:
    if not isinstance(date_str_one, str) or not isinstance(date_str_two, str):
        raise TypeError("Both arguments must be strings")
    try:
        parsed_one = datetime.strptime(date_str_one, DATE_FORMAT)
    except ValueError as exc:
        raise ValueError(f"Invalid date format for first argument: {date_str_one}") from exc
    try:
        parsed_two = datetime.strptime(date_str_two, DATE_FORMAT)
    except ValueError as exc:
        raise ValueError(f"Invalid date format for second argument: {date_str_two}") from exc
    total_seconds = (parsed_two - parsed_one).total_seconds()
    return int(total_seconds / 86400)

if __name__ == '__main__':
    first = '2020-01-01'
    second = '2020-04-01'
    difference = days_between(first, second)
    print(difference)