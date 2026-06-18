import datetime
def is_valid_date(date_str: str) -> bool:
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d") is not None
    except ValueError:
        return False
def calculate_days_between(d1_str: str, d2_str: str) -> int:
    if not is_valid_date(d1_str):
        raise ValueError(f"Invalid date format or impossible date for {d1_str}")
    if not is_valid_date(d2_str):
        raise ValueError(f"Invalid date format or impossible date for {d2_str}")
    d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
    return abs((d2 - d1).days)
if __name__ == '__main__':
    sample_dates_1 = "2023-04-30"
    sample_dates_2 = "2023-06-30"
    try:
        days_diff = calculate_days_between(sample_dates_1, sample_dates_2)
        print(f"Days between {sample_dates_1} and {sample_dates_2}: {days_diff}")
    except ValueError as e:
        print(e)