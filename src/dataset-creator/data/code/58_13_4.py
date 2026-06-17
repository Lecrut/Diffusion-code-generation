import datetime
def calculate_days_difference(date1_str: str, date2_str: str) -> int:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        return abs((dt2 - dt1).days)
    except ValueError as e:
        raise ValueError(f"Invalid date format or out of range. Error: {e}")
if __name__ == '__main__':
    sample_date_1 = "2023-05-17"
    sample_date_2 = "2024-08-29"
    try:
        result = calculate_days_difference(sample_date_1, sample_date_2)
        print(f"Difference between {sample_date_1} and {sample_date_2}: {result} days")
    except ValueError as ve:
        print(ve)