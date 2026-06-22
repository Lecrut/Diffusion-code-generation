import datetime

def is_weekday(date_value):
    if isinstance(date_value, str):
        try:
            parsed_date = datetime.datetime.strptime(date_value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_value}")
    elif isinstance(date_value, datetime.date):
        parsed_date = date_value
    else:
        raise ValueError(f"Unsupported type: {type(date_value)}")
    
    return parsed_date.weekday() < 5

if __name__ == '__main__':
    sample_date = "2023-10-23"
    result = is_weekday(sample_date)
    print(result)