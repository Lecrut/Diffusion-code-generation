from datetime import datetime

def is_earlier(date1: datetime, date2: datetime) -> bool:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be instances of datetime.")
    return date1 < date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 2)
    print(is_earlier(sample_date1, sample_date2))