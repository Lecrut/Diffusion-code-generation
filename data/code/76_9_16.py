import datetime

def calculate_days_between(date_str1: str, date_str2: str) -> int:
    date_format = "%Y-%m-%d"
    start_date = datetime.datetime.strptime(date_str1, date_format).date()
    end_date = datetime.datetime.strptime(date_str2, date_format).date()
    return abs((end_date - start_date).days)

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-05-15"
    days_difference = calculate_days_between(sample_date1, sample_date2)
    print(f"Days between {sample_date1} and {sample_date2}: {days_difference}")