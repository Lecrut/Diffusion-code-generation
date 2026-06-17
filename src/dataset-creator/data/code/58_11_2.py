import datetime
def calculate_day_difference(start: str | datetime.datetime, end: str | datetime.datetime) -> int:
    try:
        if isinstance(start, (str,)):
            start = datetime.datetime.strptime(start, "%Y-%m-%d")
        elif not isinstance(start, datetime.datetime):
            raise ValueError("Start date must be a string or datetime object.")
        if isinstance(end, (str,)):
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
        elif not isinstance(end, datetime.datetime):
            raise ValueError("End date must be a string or datetime object.")
        return int((end - start).days)
    except Exception as e:
        raise RuntimeError(f"Date calculation failed due to error: {e}")
if __name__ == '__main__':
    result = calculate_day_difference("2023-10-05", "2024-01-15")
    print(result)