from datetime import datetime

def is_earlier(date1: datetime, date2: datetime) -> bool:
    return date1 < date2

if __name__ == '__main__':
    SAMPLE_DATE1 = datetime(2023, 9, 1)
    SAMPLE_DATE2 = datetime(2023, 10, 15)
    print(is_earlier(SAMPLE_DATE1, SAMPLE_DATE2))