from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    date_format = '%Y-%m-%d'
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = abs((b - a).days)
    return delta

if __name__ == '__main__':
    print(date_difference('2023-04-01', '2023-03-15'))