import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error details: {e}")
    delta = abs(dt1 - dt2)
    return delta.days
if __name__ == '__main__':
    sample_date_1 = "2023-05-17"
    sample_date_2 = "2024-06-28"
    days_diff = calculate_days_between(sample_date_1, sample_date_2)
    print(days_diff)