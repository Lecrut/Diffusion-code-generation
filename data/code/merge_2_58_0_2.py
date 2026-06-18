import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        delta = abs((date2 - date1).days)
        return delta
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error details: {e}")
if __name__ == '__main__':
    sample_date_1 = "2023-10-05"
    sample_date_2 = "2024-01-15"
    try:
        days_diff = calculate_days_between(sample_date_1, sample_date_2)
        print(f"The number of days between {sample_date_1} and {sample_date_2} is {days_diff}.")
    except ValueError as ve:
        print(ve)