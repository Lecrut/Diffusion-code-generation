import datetime

def compute_weekday_index(date_string: str) -> int:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if not date_string:
        raise ValueError("Input string cannot be empty")
    try:
        parsed_date = datetime.date.fromisoformat(date_string)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e
    return parsed_date.weekday()

if __name__ == '__main__':
    target_date = '2024-07-04'
    weekday_index = compute_weekday_index(target_date)
    print(weekday_index)