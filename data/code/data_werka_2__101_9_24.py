import datetime

def _validate_date_input(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Date input must be a string")
    if len(date_string) != 10:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date string: {date_string}")

def get_day_of_week(date_string):
    _validate_date_input(date_string)
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return parsed_date.strftime("%A").upper()

if __name__ == '__main__':
    sample_date = "2023-11-11"
    output = get_day_of_week(sample_date)
    print(output)