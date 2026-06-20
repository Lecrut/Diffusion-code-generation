from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    date_obj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_timestamp = '2023-10-06 14:30:00'
    print(is_weekday(sample_timestamp))