import datetime

def _validate_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) != 10:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format")
    return True

def check_is_weekday(date_str):
    _validate_date_string(date_str)
    parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return parsed_date.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    results = [check_is_weekday(d) for d in sample_dates]
    print(results)