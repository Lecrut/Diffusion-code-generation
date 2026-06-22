import datetime

DATE_FORMAT = "%Y-%m-%d"

def is_date_weekday(date_string):
    try:
        parsed_date = datetime.datetime.strptime(date_string, DATE_FORMAT)
        return parsed_date.weekday() < 5
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

def has_any_weekday(date_list):
    if not date_list:
        return False
    return any(is_date_weekday(d) for d in date_list)

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    result = has_any_weekday(sample_dates)
    print(result)