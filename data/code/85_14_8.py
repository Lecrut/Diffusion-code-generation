from datetime import datetime

def validate_dates(date1, date2):
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be instances of datetime.")
    return date1, date2

def weeks_difference(date1, date2):
    date1, date2 = validate_dates(date1, date2)
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 2, 14)
    print(weeks_difference(sample_date1, sample_date2))