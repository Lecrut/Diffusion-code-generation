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
        raise RuntimeError("Date parsing failed." + str(e))
if __name__ == '__main__':
    sample_start_str = "2023-10-05T08:30:00"
    sample_end_obj = datetime.datetime(2024, 1, 15)
    result = calculate_day_difference(sample_start_str, sample_end_obj)
    print(result)