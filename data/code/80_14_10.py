from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    dt1 = datetime.strptime(date_str1, date_format)
    dt2 = datetime.strptime(date_str2, date_format)
    if dt1 < dt2:
        return -1
    elif dt1 > dt2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = compare_dates('2023-04-01', '2023-05-01')
    print(result)