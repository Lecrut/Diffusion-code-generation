import datetime

def is_weekday(date_value):
    if isinstance(date_value, str):
        try:
            parsed_date = datetime.datetime.strptime(date_value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_value}")
        date_obj = parsed_date
    elif isinstance(date_value, datetime.date):
        date_obj = date_value
    else:
        raise ValueError(f"Unsupported type: {type(date_value)}")

    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date_str = "2023-10-07"
    result = is_weekday(sample_date_str)
    print(result)