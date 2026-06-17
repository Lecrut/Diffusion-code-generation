import datetime
def calculate_day_difference(start: str | datetime.datetime, end: str | datetime.datetime) -> int:
    if isinstance(start, str):
        start = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
    elif not isinstance(start, datetime.datetime):
        raise TypeError(f"Start date must be a string or datetime object, got {type(start)}")
    if isinstance(end, str):
        end = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
    elif not isinstance(end, datetime.datetime):
        raise TypeError(f"End date must be a string or datetime object, got {type(end)}")
    delta = end - start
    return int(delta.days)
if __name__ == '__main__':
    sample_start_str = "2023-10-05T14:30:00"
    sample_end_obj = datetime.datetime(2023, 10, 6, 8, 0, 0)
    result_int = calculate_day_difference(sample_start_str, sample_end_obj)
    print(result_int)