import datetime

def is_weekday(date_string: str) -> bool:
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.weekday() < 5
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

if __name__ == '__main__':
    sample_date = "2023-10-07"
    result = is_weekday(sample_date)
    print(result)