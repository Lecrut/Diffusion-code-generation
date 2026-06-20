from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def compare_dates(date_str1: str, date_str2: str) -> int:
    date1 = datetime.strptime(date_str1, DATE_FORMAT)
    date2 = datetime.strptime(date_str2, DATE_FORMAT)
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-04-02'))
    print(compare_dates('2023-04-02', '2023-04-01'))
    print(compare_dates('2023-04-01', '2023-04-01'))