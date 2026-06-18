import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        if dt1 > dt2:
            return -(dt2 - dt1).days
        delta = (dt2 - dt1)
        days_difference = abs(delta.days)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got {e}") from None
    return days_difference
if __name__ == '__main__':
    sample_date_1 = "2023-05-17"
    sample_date_2 = "2024-08-19"
    result = calculate_days_between(sample_date_1, sample_date_2)
    print(result)