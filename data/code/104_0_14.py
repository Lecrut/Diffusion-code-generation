from datetime import datetime

def compare_dates(date1: datetime, date2: datetime) -> bool:
    return date1 < date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 9, 25)
    sample_date2 = datetime(2023, 10, 26)
    result = compare_dates(sample_date1, sample_date2)
    print(result)