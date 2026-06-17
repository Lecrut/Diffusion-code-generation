import datetime
def calculate_days_delta(start: datetime.datetime | str, end: datetime.datetime | str) -> int:
    if isinstance(start, str):
        start = datetime.datetime.fromisoformat(start)
    elif not isinstance(start, datetime.datetime):
        raise TypeError("Start argument must be a string or datetime object")
    if isinstance(end, str):
        end = datetime.datetime.fromisoformat(end)
    elif not isinstance(end, datetime.datetime):
        raise TypeError("End argument must be a string or datetime object")
    delta_seconds = (end - start).total_seconds()
    return int(delta_seconds // 86400)
if __name__ == '__main__':
    test_cases: list[tuple[str, str]] = [
        ("2023-01-01", "2023-01-05"),
        ("2023-01-01 10:00:00", "2023-01-06 10:00:00"),
        (datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 7)),
    ]
    for start_str, end_str in test_cases:
        result = calculate_days_delta(start_str, end_str)
        print(f"Delta between {start_str} and {end_str}: {result} days")