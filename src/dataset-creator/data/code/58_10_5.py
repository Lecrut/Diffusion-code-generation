import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    delta = abs(dt2 - dt1)
    return delta.days
if __name__ == '__main__':
    sample_date_1 = "2023-04-05"
    sample_date_2 = "2023-12-25"
    days_diff = calculate_days_between(sample_date_1, sample_date_2)
    print(days_diff)