import datetime
def calculate_date_difference(date1_str: str, date2_str: str) -> int:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        delta_days = (dt2 - dt1).days
        return int(delta_days)
    except ValueError as e:
        raise ValueError(f"Invalid date format or out of range. Error details: {e}")
if __name__ == '__main__':
    sample_date_1 = "2023-05-17"
    sample_date_2 = "2024-08-19"
    try:
        result_days = calculate_date_difference(sample_date_1, sample_date_2)
        print(f"Difference between {sample_date_1} and {sample_date_2}: {result_days} days")
    except ValueError as ve:
        print(f"Error processing dates: {ve}")