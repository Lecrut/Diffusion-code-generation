import datetime

def parse_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

def is_weekday(date_obj):
    return date_obj.weekday() < 5

def contains_weekdays(date_strings):
    parsed_dates = [parse_date(d) for d in date_strings]
    return any(is_weekday(d) for d in parsed_dates)

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    result = contains_weekdays(sample_dates)
    print(result)