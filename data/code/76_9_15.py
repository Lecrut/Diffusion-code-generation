import datetime
DAYS_IN_YEAR = 365.25

def calculate_days_between(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    start_date = datetime.datetime.strptime(date_str1, date_format).date()
    end_date = datetime.datetime.strptime(date_str2, date_format).date()
    delta = abs((end_date - start_date).days)
    return delta
if __name__ == '__main__':
    sample_date1 = '2023-01-01'
    sample_date2 = '2024-01-01'
    days_difference = calculate_days_between(sample_date1, sample_date2)
    print(f'Days between {sample_date1} and {sample_date2}: {days_difference}')