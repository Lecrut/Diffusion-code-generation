from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

if __name__ == '__main__':
    print(date_difference('2023-04-01', '2023-04-15'))