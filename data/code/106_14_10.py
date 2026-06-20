from datetime import datetime

def years_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = datetime(1990, 5, 15)
    sample_date2 = datetime(2023, 8, 20)
    print(years_difference(sample_date1, sample_date2))