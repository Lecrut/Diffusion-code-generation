import datetime

def is_weekday(date_input):
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date string")
        return parsed.weekday() < 5
    if isinstance(date_input, datetime.date):
        return date_input.weekday() < 5
    raise ValueError("Unsupported type")

if __name__ == '__main__':
    sample = "2023-10-07"
    print(is_weekday(sample))