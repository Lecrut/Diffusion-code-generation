import datetime
def calculate_days_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError(f"Invalid date format or out of range. Error details: {e}")
if __name__ == '__main__':
    sample_date_1 = "2023-06-15"
    sample_date_2 = "2024-08-20"
    try:
        days_diff = calculate_days_difference(sample_date_1, sample_date_2)
        print(days_diff)
    except ValueError as ve:
        print(f"Error processing dates: {ve}")