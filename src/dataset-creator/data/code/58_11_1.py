import datetime
def calculate_day_difference(start: str | datetime.datetime, end: str | datetime.datetime) -> int:
    try:
        if isinstance(start, str):
            start = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
        elif not isinstance(start, datetime.datetime):
            raise ValueError(f"Invalid start date type. Expected string or datetime object.")
        if isinstance(end, str):
            end = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
        elif not isinstance(end, datetime.datetime):
            raise ValueError(f"Invalid end date type. Expected string or datetime object.")
        delta = end - start
        return int(delta.days)
    except (ValueError, TypeError) as e:
        raise RuntimeError("Date parsing failed") from e
if __name__ == '__main__':
    result = calculate_day_difference(
        "2023-10-05T08:30:00",
        "2024-01-15T14:20:00"
    )
    print(result)