import datetime
def calculate_day_difference(start_date: str | datetime.datetime, end_date: str | datetime.datetime) -> int:
    try:
        if isinstance(start_date, str):
            start_dt = datetime.datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        else:
            start_dt = start_date
        if isinstance(end_date, str):
            end_dt = datetime.datetime.fromisoformat(end_date.replace("Z", "+00:00"))
        else:
            end_dt = end_date
        delta = end_dt - start_dt
        return int(delta.days)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid date format or type. Error details: {e}")
if __name__ == '__main__':
    sample_start = "2023-10-05T08:30:00+00:00"
    sample_end = "2024-01-15T14:20:00Z"
    result = calculate_day_difference(sample_start, sample_end)
    print(result)