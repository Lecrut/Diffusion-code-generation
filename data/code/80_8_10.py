from datetime import datetime

def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, '%Y-%m-%d')

def compare_dates(date1: datetime, date2: datetime) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

def format_date(date_obj: datetime, format_str: str='%Y-%m-%d') -> str:
    return date_obj.strftime(format_str)
if __name__ == '__main__':
    date1 = parse_date('2023-10-01')
    date2 = parse_date('2023-10-15')
    print(compare_dates(date1, date2))
    print(format_date(date1))