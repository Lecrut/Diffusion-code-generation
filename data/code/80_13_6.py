from datetime import datetime

def compare_dates(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return (d1 > d2) - (d1 < d2)
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-04-02'))
    print(compare_dates('2023-04-02', '2023-04-01'))
    print(compare_dates('2023-04-01', '2023-04-01'))