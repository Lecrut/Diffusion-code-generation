import datetime
def calculate_days_delta(start: datetime.datetime | str, end: datetime.datetime | str) -> int:
    if isinstance(start, str):
        start = datetime.datetime.fromisoformat(start)
    elif not isinstance(start, datetime.datetime):
        raise TypeError("Start must be a string or datetime object")
    if isinstance(end, str):
        end = datetime.datetime.fromisoformat(end)
    elif not isinstance(end, datetime.datetime):
        raise TypeError("End must be a string or datetime object")
    delta_seconds = (end - start).total_seconds()
    return int(delta_seconds // 86400)
if __name__ == '__main__':
    test_cases = [
        ("2023-01-01", "2023-01-05"),
        (datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 4)),
        ("2023-06-15T10:00:00", "2023-06-17T10:00:00"),
    ]
    for start_input, end_input in test_cases:
        result = calculate_days_delta(start_input, end_input)
        print(f"Delta between {start_input} and {end_input}: {result} days")