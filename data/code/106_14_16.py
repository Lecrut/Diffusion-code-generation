from datetime import datetime

def year_difference(dt1: datetime, dt2: datetime) -> int:
    return abs(dt1.year - dt2.year)

if __name__ == '__main__':
    date1 = datetime(2023, 10, 15)
    date2 = datetime(2025, 5, 20)
    result = year_difference(date1, date2)
    print(result)