import datetime

def verify_weekday(date_input):
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date string: {date_input}") from e
        return parsed.weekday() < 5
    if isinstance(date_input, datetime.date):
        return date_input.weekday() < 5
    raise ValueError(f"Expected date or string, got {type(date_input)}")

if __name__ == '__main__':
    date_str = "2023-10-23"
    date_obj = datetime.date(2023, 10, 23)
    print(verify_weekday(date_str))
    print(verify_weekday(date_obj))