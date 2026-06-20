from datetime import datetime

def compare_dates(date1: str, date2: str) -> int:
    dt1 = datetime.strptime(date1, '%Y-%m-%d')
    dt2 = datetime.strptime(date2, '%Y-%m-%d')
    return (dt1 > dt2) - (dt1 < dt2)
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-04-02'))
    print(compare_dates('2023-04-01', '2023-04-01'))
    print(compare_dates('2023-04-02', '2023-04-01'))