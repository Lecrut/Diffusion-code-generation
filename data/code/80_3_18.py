from datetime import datetime

def is_strictly_before(date1: datetime, date2: datetime) -> bool:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError('Both arguments must be instances of datetime.')
    return date1 < date2
if __name__ == '__main__':
    try:
        date1 = datetime(2023, 10, 26)
        date2 = datetime(2023, 10, 20)
        print(is_strictly_before(date1, date2))
    except ValueError as e:
        print(e)