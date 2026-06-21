import datetime

def compute_weekday_index(date_string):
    if not isinstance(date_string, str):
        raise ValueError("date_string must be a string")
    try:
        parsed_date = datetime.date.fromisoformat(date_string)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")
    return parsed_date.weekday()

if __name__ == '__main__':
    _DATE = "2024-07-04"
    _result = compute_weekday_index(_DATE)
    print(_result)