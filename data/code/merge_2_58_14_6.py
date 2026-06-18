import datetime
def is_valid_date(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    if not is_valid_date(date1_str):
        raise ValueError(f"Invalid date format for {date1_str}. Expected YYYY-MM-DD.")
    if not is_valid_date(date2_str):
        raise ValueError(f"Invalid date format for {date2_str}. Expected YYYY-MM-DD.")
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError(f"Date parsing failed for one of the inputs.") from e
    delta = abs((date2 - date1).days)
    return delta
if __name__ == '__main__':
    sample_date_1 = "2023-05-17"
    sample_date_2 = "2024-08-19"
    try:
        days_diff = calculate_days_between(sample_date_1, sample_date_2)
        print(f"The number of days between {sample_date_1} and {sample_date_2} is {days_diff}.")
    except ValueError as ve:
        print(f"Error: {ve}")