from datetime import datetime

def is_earlier(first: datetime, second: datetime) -> bool:
    return first < second

if __name__ == '__main__':
    date1 = datetime(2023, 1, 1, 12, 0, 0)
    date2 = datetime(2023, 1, 2, 12, 0, 0)
    result = is_earlier(date1, date2)
    print(result)