import datetime

def calculate_days_between_dates(start_date_str: str, end_date_str: str) -> int:
    date_format = "%Y-%m-%d"
    start_date = datetime.datetime.strptime(start_date_str, date_format).date()
    end_date = datetime.datetime.strptime(end_date_str, date_format).date()
    return abs((end_date - start_date).days)

if __name__ == '__main__':
    sample_start_date = "2023-01-01"
    sample_end_date = "2024-01-01"
    days_difference = calculate_days_between_dates(sample_start_date, sample_end_date)
    print(f"Days between {sample_start_date} and {sample_end_date}: {days_difference}")