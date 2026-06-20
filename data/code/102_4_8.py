from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return dt.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-06 14:30:00'))
    print(is_weekday('2023-10-07 14:30:00'))