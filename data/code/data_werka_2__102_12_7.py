import datetime

def is_weekday(date_input):
    if isinstance(date_input, str):
        try:
            parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_input}")
    elif isinstance(date_input, datetime.date):
        parsed_date = date_input
    else:
        raise ValueError(f"Unsupported type: {type(date_input)}")
    
    return parsed_date.weekday() < 5

if __name__ == '__main__':
    sample_date_str = "2023-10-07"
    result = is_weekday(sample_date_str)
    print(result)