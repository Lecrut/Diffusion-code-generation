from datetime import datetime

def is_earlier(date1: datetime, date2: datetime) -> bool:
    return date1 < date2

if __name__ == '__main__':
    d1 = datetime(2023, 1, 1, 12, 0, 0)
    d2 = datetime(2023, 1, 2, 12, 0, 0)
    print(is_earlier(d1, d2))