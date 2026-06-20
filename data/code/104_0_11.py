from datetime import datetime

def is_earlier(date1: datetime, date2: datetime) -> bool:
    return date1 < date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 5, 1)
    sample_date2 = datetime(2023, 6, 1)
    result = is_earlier(sample_date1, sample_date2)
    print(result)