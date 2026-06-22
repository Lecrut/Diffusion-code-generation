import datetime

def is_weekday(date_value):
    if isinstance(date_value, datetime.date):
        return date_value.weekday() < 5
    if isinstance(date_value, str):
        try:
            parsed_date = datetime.datetime.strptime(date_value, "%Y-%m-%d").date()
            return parsed_date.weekday() < 5
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_value}")
    raise ValueError(f"Unsupported type: {type(date_value)}")

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 23)
    sample_date_str = "2023-10-23"
    sample_weekend = datetime.date(2023, 10, 21)
    
    result1 = is_weekday(sample_date)
    result2 = is_weekday(sample_date_str)
    result3 = is_weekday(sample_weekend)
    
    print(result1)
    print(result2)
    print(result3)