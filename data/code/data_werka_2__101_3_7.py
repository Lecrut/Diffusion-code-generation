import datetime

def get_weekday(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        return parsed_date.weekday()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e

if __name__ == '__main__':
    target_date = "2023-12-25"
    weekday_index = get_weekday(target_date)
    print(weekday_index)