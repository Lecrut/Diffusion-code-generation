from datetime import datetime

def weeks_difference(date1: datetime, date2: datetime) -> int:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be instances of datetime")
    
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 15)
    print(weeks_difference(sample_date1, sample_date2))