from datetime import datetime

WEEKDAY_FORMAT = "%Y-%m-%d"

def parse_date_string(date_str):
    try:
        return datetime.strptime(date_str, WEEKDAY_FORMAT)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def is_weekday(date_obj):
    return date_obj.weekday() < 5

def contains_weekdays(date_strings):
    parsed_dates = [parse_date_string(ds) for ds in date_strings]
    weekday_flags = [is_weekday(d) for d in parsed_dates]
    return any(weekday_flags)

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    result = contains_weekdays(sample_dates)
    print(result)