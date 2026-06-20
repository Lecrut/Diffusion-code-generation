from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    date_obj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return date_obj.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-04 12:30:45'))
    print(is_weekday('2023-10-07 12:30:45'))