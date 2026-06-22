import datetime

def calculate_weekday_for_date(date_string):
    if not isinstance(date_string, str):
        raise ValueError("date_string must be a string")
    try:
        parsed_date = datetime.date.fromisoformat(date_string)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")
    return parsed_date.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    weekday_index = calculate_weekday_for_date(sample_date)
    print(weekday_index)