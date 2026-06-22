import datetime

def is_weekday(date_string: str) -> bool:
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")
    
    return parsed_date.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2023-10-23", "2023-10-21", "invalid-date"]
    for date_str in sample_dates:
        try:
            result = is_weekday(date_str)
            print(result)
        except ValueError as e:
            print(e)