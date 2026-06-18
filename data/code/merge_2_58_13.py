import datetime
def calculate_days_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")
if __name__ == '__main__':
    sample_date_1 = "2023-05-15"
    sample_date_2 = "2024-08-20"
    try:
        diff_days = calculate_days_difference(sample_date_1, sample_date_2)
        print(diff_days)
    except ValueError as ve:
        print(f"Error processing dates: {ve}")