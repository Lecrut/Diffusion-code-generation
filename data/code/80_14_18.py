from datetime import datetime

def compare_dates(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    if d1 < d2:
        return -1
    elif d1 > d2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-05-01'))
    print(compare_dates('2023-06-01', '2023-05-01'))
    print(compare_dates('2023-05-01', '2023-05-01'))