import datetime
def calculate_day_difference(start: str | datetime.datetime, end: str | datetime.datetime) -> int:
    if isinstance(start, str):
        start = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
    elif not isinstance(start, datetime.datetime):
        raise TypeError(f"Start date must be a string or datetime object, got {type(start).__name__}")
    if isinstance(end, str):
        end = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
    elif not isinstance(end, datetime.datetime):
        raise TypeError(f"End date must be a string or datetime object, got {type(end).__name__}")
    delta = end - start
    return int(delta.days)
if __name__ == '__main__':
    result = calculate_day_difference("2023-10-05", "2024-01-15")
    print(result)